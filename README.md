# Soundboard Application

This is a simple Python-based soundboard application that allows users to play sound files from a specified folder, stop playback, and get a list of available audio input devices. It uses the `pygame` library for audio playback and `sounddevice` for listing audio devices.

## Features

- **Play Sound:** Allows the user to play sound files from a `sounds` folder.
- **Stop Sound:** Stops any currently playing sound.
- **Get Audio Devices:** Displays a list of available audio input and output devices.
- **Dynamic Folder Creation:** The application automatically creates a `sounds` folder in the same directory as the executable (or script) if it doesn't exist.

## Requirements

- Python 3.x
- `pygame` library
- `sounddevice` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/soundboard.git
    cd soundboard
    ```

2. Install the required dependencies:

    ```bash
    pip install pygame sounddevice
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Once the program is running, you can use the following commands:
    - `play`: Prompts you to choose a sound file to play from the `sounds` folder.
    - `stop`: Stops the currently playing sound.
    - `getaudiodivice`: Lists all available audio input/output devices.
    - `help`: Displays a list of available commands.

## How It Works

1. The program initializes the Pygame mixer with a default audio device (e.g., CABLE Input).
2. The `setUp()` function checks if the `sounds` folder exists in the same directory as the executable. If not, it creates the folder.
3. The user is prompted to enter a command to play, stop music, or list available devices.

## Folder Structure

- `main.py`: The main script for the soundboard application.
- `sounds/`: A folder (automatically created) where sound files are stored.

## Example Commands

```bash
Commands: play,getaudiodivice,stop
Write a command: play
Input the number of the file to play: 0
Now playing: example_sound.wav

Write a command: stop
Music stopped.

Write a command: getaudiodivice
Available audio devices:
0: Microphone (Realtek High Defini (Input)
1: Speakers (Realtek High Definition Audio) (Output)
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### How to Use This Template:

1. **Repository Information:** Replace `yourusername` in the clone URL with your GitHub username.
2. **Dependencies:** Make sure your `requirements.txt` (if using) includes `pygame` and `sounddevice`.
3. **Additional Details:** Feel free to customize the sections like features, installation, and usage according to your exact implementation.

This `README.md` provides a clear overview of how to set up, use, and extend the project.
