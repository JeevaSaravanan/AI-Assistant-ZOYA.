# web_utils.py

import webbrowser
from constants import APP_NAMES, APP_URLS
from speech_utils import speak

def open_website(command):
    for name, url in zip(APP_NAMES, APP_URLS):
        if name.lower() in command:
            speak(f"Opening {name}")
            webbrowser.open_new_tab(f"http://{url}")
            return True
    return False
