import requests

# Replace with your pCloud credentials
pcloud_username = ''
pcloud_password = 'your_password'

# Authenticate with pCloud
def authenticate(username, password):
    response = requests.post('https://api.pcloud.com/login', data={'username': username, 'password': password})
    return response.json()

# Main function
def main():
    auth_response = authenticate(pcloud_username, pcloud_password)
    if 'auth' in auth_response:
        print("Authentication successful! Auth token:", auth_response['auth'])
    else:
        print("Authentication failed:", auth_response)

if __name__ == "__main__":
    main()
