import requests

# Replace with your pCloud account information
pcloud_username = 'teamsosiut21@gmail.com'  # Your Gmail or pCloud username
pcloud_app_password = 'sosteam21'  # The application password you generated

# Authenticate with pCloud
def authenticate(username, app_password):
    response = requests.post('https://api.pcloud.com/login', data={'username': username, 'password': app_password})
    return response.json()

# List folders in the root directory
def list_folders(auth_token):
    response = requests.post('https://api.pcloud.com/listfolder', data={'auth': auth_token, 'path': '/'})
    return response.json()

# Main function
def main():
    # Step 1: Authenticate
    auth_response = authenticate(pcloud_username, pcloud_app_password)
    
    if 'auth' in auth_response:
        auth_token = auth_response['auth']
        print("Authentication successful! Auth token:", auth_token)

        # Step 2: List folders
        folders_response = list_folders(auth_token)
        
        if 'folders' in folders_response:
            print("Folders in your pCloud account:")
            for folder in folders_response['folders']:
                print("-", folder['name'])
        else:
            print("No folders found or an error occurred:", folders_response)
    else:
        print("Authentication failed:", auth_response)

if __name__ == "__main__":
    main()
