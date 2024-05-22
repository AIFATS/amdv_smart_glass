import os
import pygame

"""
play the ringtones audio
"""

# Define the directory path
directory_path = 'File_Management/config/Ringtone_&_notification/ringtones'

def play_audio(file_name):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Construct the full file path
    file_path = os.path.join(directory_path, file_name + '.ogg')

    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Load and play the audio file
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            print(f"Now playing: {file_name}")
            
            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                continue
        except Exception as e:
            print(f"Error playing audio: {e}")
    else:
        print(f"File not found: {file_name}")

if __name__ == "__main__":
    # Take input for the file name
    file_name = input("Enter the file name (without extension): ")
    
    # Play the audio file
    play_audio(file_name)
