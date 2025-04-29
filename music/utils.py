# music/utils.py

import requests
import os
from django.conf import settings
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from django.core.files.storage import FileSystemStorage


def authenticate():
    """
    Authenticate with pCloud and return an auth token.
    """
    response = requests.post(
        f"{settings.PCLOUD_API_BASE_URL}/login",
        data={'username': settings.PCLOUD_USERNAME, 'password': settings.PCLOUD_PASSWORD}
    )
    auth_data = response.json()
    if 'auth' in auth_data:
        return auth_data['auth']
    else:
        raise Exception("Failed to authenticate with pCloud: " + auth_data.get('error', 'Unknown error'))


def upload_to_pcloud(mp3_file):
    """
    Upload the MP3 file to a specific folder in pCloud.
    """
    upload_url = "https://api.pcloud.com/uploadfile"  # pCloud upload endpoint
    auth_token = authenticate()  # Get the authentication token from pCloud
    folder_id = "23361959698"  # pCloud folder ID where the file will be uploaded

    # File name from the file object
    file_name = mp3_file.name  # Original file name
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # Save the uploaded file to the local media folder
    with open(file_path, 'wb') as f:
        for chunk in mp3_file.chunks():
            f.write(chunk)

    try:
        # Prepare the payload to upload to pCloud
        with open(file_path, 'rb') as f:
            files = {'file': (file_name, f, 'audio/mpeg')}
            data = {
                'auth': auth_token,  # pCloud authentication token
                'folderid': folder_id  # Folder ID where the file will be uploaded
            }

            # Send the file to pCloud
            response = requests.post(upload_url, files=files, data=data, timeout=60)

        # Check if the upload was successful
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("result") == 0:
                # If successful, return the URL or some identifier
                file_url = response_json.get("filelink")
                print(f"File uploaded successfully. File URL: {file_url}")
                return file_url
            else:
                print(f"Upload failed with result: {response_json.get('result')}")
                return None
        else:
            print(f"Failed to upload file. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
        return None

    finally:
        # Optionally remove the file from local storage after uploading
        if os.path.exists(file_path):
            os.remove(file_path)


def list_folder_contents(path=settings.PCLOUD_MUSIC_FOLDER):
    """
    List the contents of a pCloud folder.
    """
    auth_token = authenticate()
    response = requests.post(
        f"{settings.PCLOUD_API_BASE_URL}/listfolder",
        data={'auth': auth_token, 'path': path}
    )
    return response.json()

def download_file(file_path, local_path):
    """
    Download a file from pCloud to a local path.
    """
    auth_token = authenticate()
    response = requests.post(
        f"{settings.PCLOUD_API_BASE_URL}/getfilelink",
        data={'auth': auth_token, 'path': file_path}
    )
    file_data = response.json()
    if file_data.get('result') != 0:
        raise Exception("Failed to get download link from pCloud: " + file_data.get('error', 'Unknown error'))

    download_url = f"https://{file_data['hosts'][0]}{file_data['path']}"
    download_response = requests.get(download_url, stream=True)

    if download_response.status_code == 200:
        with open(local_path, 'wb') as file:
            for chunk in download_response.iter_content(chunk_size=8192):
                file.write(chunk)
        return local_path
    else:
        raise Exception("Failed to download file from pCloud, status code: " + str(download_response.status_code))
