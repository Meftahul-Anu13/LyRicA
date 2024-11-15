# music/utils.py

import requests
import os
from django.conf import settings

def authenticate():
    """
    Authenticate with pCloud and return an auth token.
    """
    response = requests.post(
        f"{settings.PCLOUD_API_BASE_URL}/login",
        data={'username': settings.PCLOUD_USERNAME, 'password': settings.PCLOUD_APP_PASSWORD}
    )
    auth_data = response.json()
    if 'auth' in auth_data:
        return auth_data['auth']
    else:
        raise Exception("Failed to authenticate with pCloud: " + auth_data.get('error', 'Unknown error'))

def upload_to_pcloud(file_path, file_name):
    """
    Upload a file to pCloud.
    """
    auth_token = authenticate()
    url = f"{settings.PCLOUD_API_BASE_URL}/uploadfile"
    with open(file_path, 'rb') as file:
        files = {'file': (file_name, file)}
        data = {'auth': auth_token, 'folderid': settings.PCLOUD_SONG_FOLDER}
        response = requests.post(url, files=files, data=data)
    
    response_data = response.json()
    if response_data.get('result') == 0:
        return response_data.get('fileids', [None])[0]
    else:
        raise Exception("Failed to upload to pCloud: " + response_data.get('error', 'Unknown error'))

def list_folder_contents(path=settings.PCLOUD_SONG_FOLDER):
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
