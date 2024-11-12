import requests

# Replace with your pCloud account information
pcloud_username = 'teamsosiut21@gmail.com'  # Your Gmail or pCloud username
pcloud_app_password = 'sosteam21'  # The application password you generated

# Authenticate with pCloud
def authenticate(username, app_password):
    response = requests.post('https://api.pcloud.com/login', data={'username': username, 'password': app_password})
    return response.json()

# Upload file to pCloud
def upload_file(auth_token, file_path, target_folder_path):
    upload_url = "https://api.pcloud.com/uploadfile"
    files = {
        'file': open(file_path, 'rb')  # Open the file to upload in binary mode
    }
    data = {
        'auth': auth_token,  # Auth token from login
        'folderid': target_folder_path  # Target folder ID or path
    }
    
    response = requests.post(upload_url, files=files, data=data)
    return response.json()

# Main function
def main():
    # Step 1: Authenticate
    auth_response = authenticate(pcloud_username, pcloud_app_password)
    
    if 'auth' in auth_response:
        auth_token = auth_response['auth']
        print("Authentication successful! Auth token:", auth_token)

        # Step 2: Specify the local file path and the pCloud target folder
        local_file_path = 'song.mp3'  # Path to the file you want to upload
        target_folder_path = '/My Music'  # Path or folder ID where you want to upload the file

        # Step 3: Upload the file
        upload_response = upload_file(auth_token, local_file_path, target_folder_path)
        
        # Step 4: Check the upload result
        if 'metadata' in upload_response:
            print(f"File uploaded successfully to {target_folder_path}")
        else:
            print("File upload failed:", upload_response)
    else:
        print("Authentication failed:", auth_response)

if __name__ == "__main__":
    main()
