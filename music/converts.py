
import requests
import os
import pygame
from time import sleep
# Replace with your pCloud account information
import requests
import os
import pygame
from time import sleep

# Replace with your pCloud account information
pcloud_username = 'teamsosiut21@gmail.com'  # Your Gmail or pCloud username
pcloud_app_password = 'sosteam21'  # The application password you generated

# Authenticate with pCloud
def authenticate(username, app_password):
    response = requests.post('https://api.pcloud.com/login', data={'username': username, 'password': app_password})
    return response.json()

# List contents of the specified folder
def list_folder_contents(auth_token, path='/'):
    response = requests.post('https://api.pcloud.com/listfolder', data={'auth': auth_token, 'path': path})
    return response.json()

# Download file from pCloud
def download_file(auth_token, file_path, local_path):
    response = requests.post('https://api.pcloud.com/getfilelink', data={'auth': auth_token, 'path': file_path})
    
    # Debugging: Print the response content
    print("Response from getfilelink:", response.json())  # Print the raw response

    result = response.json()
    
    # Check if the result indicates an error
    if isinstance(result, dict) and 'result' in result and result['result'] != 0:
        print("Error fetching file link:", result.get('error'))  # Print error message if present
        return None

    # Use the path directly from the response for download
    download_url = f"https://{result['hosts'][0]}{result['path']}"

    # Perform the download in chunks
    r = requests.get(download_url, stream=True)
    if r.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):  # Download in chunks
                f.write(chunk)
        print(f'Downloaded: {local_path}')  # Corrected print statement
        return local_path
    else:
        print("Failed to download the file, status code:", r.status_code)
        return None

# Main function
def main():
    # Step 1: Authenticate
    auth_response = authenticate(pcloud_username, pcloud_app_password)
    
    if 'auth' in auth_response:
        auth_token = auth_response['auth']
        print("Authentication successful! Auth token:", auth_token)

        # Step 2: List contents in "My Music" folder
        music_folder_path = '/My Music'  # Specify the path to your music folder
        music_contents_response = list_folder_contents(auth_token, music_folder_path)
        
        if 'contents' in music_contents_response.get('metadata', {}):
            print("Songs in 'My Music' folder:")
            for item in music_contents_response['metadata']['contents']:
                if not item['isfolder']:  # Check if the item is a file (not a folder)
                    print("-", item['name'])
                    
                    # Play the Momentum.mp3 if found
                    if item['name'] == 'Demo Audio 2.mp3':
                        # Step 3: Download the file
                        local_file_path = os.path.join(os.getcwd(), 'Momentum.mp3')
                        download_file(auth_token, item['path'], local_file_path)
                        
                        # Step 4: Play the downloaded audio file using Pygame
                        pygame.mixer.init()  # Initialize the mixer module
                        pygame.mixer.music.load(local_file_path)  # Load the music file
                        pygame.mixer.music.play()  # Play the music
                        
                        # Keep the script running until the music stops
                        while pygame.mixer.music.get_busy():
                            sleep(1)
                        break  # Exit after playing the song
        else:
            print("No songs found in 'My Music' or an error occurred:", music_contents_response)
    else:
        print("Authentication failed:", auth_response)

if __name__ == "__main__":
    main()
