from mega import Mega
import pygame
import time

# Initialize Mega instance
mega = Mega()
email = "teamsosiut21@gmail.com"
password = "sosteam21"

# Log in to MEGA
mega_login = mega.login(email, password)

# Fetch files and print the structure of each file's info to identify the correct keys
files = mega_login.get_files()

# Print the file information to find the correct key for the name
for file_id, info in files.items():
    print(f"File ID: {file_id}, Info: {info}")

# Now find the MP3 file based on the correct key
file_name = 'song1.mp3'
file = None

for file_id, info in files.items():
    # Based on the printed structure, modify this key path if necessary
    if 'name' in info and info['name'] == file_name:
        print(f"Found the file: {info['name']}")
        file = mega_login.download(info)
        break

if file:
    # Initialize pygame for playback
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Keep the script running while the song plays
    while pygame.mixer.music.get_busy():
        time.sleep(1)
else:
    print("MP3 file not found.")
