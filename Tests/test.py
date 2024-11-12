import pygame
import time

def play_song(file_path):
    # Initialize the mixer module
    pygame.mixer.init()
    # Load the mp3 file
    pygame.mixer.music.load(file_path)
    # Play the song
    pygame.mixer.music.play()
    
    # Keep the program running until the song finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Replace 'song.mp3' with your mp3 file path
play_song("song.mp3")
