# Soundboard Application

This Python application allows you to manage and play audio files from a specific folder. It uses **Pygame** for audio playback and **Sounddevice** for listing available audio devices.

## Features
- **Play Sound**: Choose a sound file from a predefined folder and play it.
- **Stop Music**: Stop any sound currently playing.
- **Get Audio Devices**: List all available input and output audio devices on your system.
- **Help**: Displays information about the available commands.

## Requirements
Before running this program, make sure you have the following libraries installed:
- **pygame**
- **sounddevice**

You can install them using `pip`:

```bash
pip install pygame sounddevice
```

## Usage

### Running the Program
Run the Python script (`main.py`) and interact with the program via the command line. The program will prompt you to enter a command.

### Commands
- **play**: Plays a selected audio file from the folder.
- **stop**: Stops the currently playing audio.
- **getaudiodivice**: Lists available audio devices on your system.
- **help**: Displays a list of available commands.

### Example Commands
1. **play**: 
   - When prompted, enter the number corresponding to the file you want to play (from the list of available files in the folder).

2. **getaudiodivice**: 
   - Lists all available audio devices (input/output).

3. **stop**:
   - Stops the music that is currently playing.

### Folder Setup
- Make sure you have a folder containing audio files (e.g., `.mp3` or `.wav` format).
- Update the `folder_path` variable in the code to match the location of your sound files.

```python
folder_path = "C:/Users/nir/Desktop/sounds"  # Replace with your actual folder path
```

### Example of Running the Program

```bash
Commands: play, getaudiodivice, stop
Write a command: getaudiodivice
Available audio devices:
0: Microsoft Sound Mapper - Input (Input)
1: Microphone (Realtek High Definition) (Input)
...
```

```bash
Commands: play, getaudiodivice, stop
Write a command: play
Files in the folder:
File number 0: sound1.wav
File number 1: sound2.wav
...
Input the number of the file to play: 1
Now playing: sound2.wav
```

## Notes
- The program requires you to have audio files in the specified folder path for the "play" command to work.
- The program uses **VB-Audio Virtual Cable** for output (you can change it to your desired device if needed).

## License
This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.
