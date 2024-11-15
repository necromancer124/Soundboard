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

This project is licensed under the MIT License - see the LICENSE file for details.
---

**Credits:**
- Author: [Nir Smidov]
- License: MIT License

