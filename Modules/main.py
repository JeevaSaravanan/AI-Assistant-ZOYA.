# main.py

from assistant import welcome, process_command
from speech_utils import get_audio

if __name__ == "__main__":
    welcome()
    while True:
        command = get_audio()
        if command:
            print(f"You said: {command}")
            process_command(command)
