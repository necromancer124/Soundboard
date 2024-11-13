import os
import pygame
import sounddevice as sd

# Initialize the Pygame mixer
pygame.mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

def main(command):
    if command == "play":
        play()
    elif command.lower() == "getaudiodivice":
        get_audio_device()
    elif command.lower() == "stop":
        stop_music()
    elif command.lower() == "help":
        help()
    else:
        print("Invalid command!")

def play():
    files_list = print_all()
    try:
        # Get user input for the file index
        file_index = int(input("Input the number of the file to play: "))
        if file_index < 0 or file_index >= len(files_list):
            print("Invalid file number.")
            return
        #the path to my sounds folder:
        file_path = "C:/Users/nir/Desktop/sounds/" + files_list[file_index]  # replace with your absolute path

        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {files_list[file_index]}")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("File number out of range.")

def print_all():
    folder_path = "C:/Users/nir/Desktop/sounds"

    # Get a list of all file names in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    print("Files in the folder:")
    for x, file in enumerate(files):
        print(f"File number {x}: {file}")

    return files

def stop_music():
    # Stop the music
    pygame.mixer.music.stop()
    print("Music stopped.")

def get_audio_device():
    # List all available devices
    devices = sd.query_devices()
    print("Available audio devices:")
    for i, device in enumerate(devices):
        print(f"{i}: {device['name']} ({'Input' if device['max_input_channels'] > 0 else 'Output'})")

def help():
    print("command play:\n allows you to play the sounds of your choice from the folder\n\n command stop:\n stops the music playing\n\ncommand getaudiodivice:\nshows the available audio \n#####################")
####################################
while True:
    command = input("\nCommands: play,getaudiodivice,stop\nWrite a command:")
    main(command)