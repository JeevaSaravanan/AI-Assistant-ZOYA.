# assistant.py

import random
from constants import GREETINGS, RESPONSES
from speech_utils import speak
from web_utils import open_website
from wolfram_utils import wolfram_search
from llm_utils import ask_llm

def welcome():
    speak("Hello, how can I help you?")

def greet_user():
    speak(random.choice(RESPONSES))

def process_command(command):
    if command is None:
        return
    if command in GREETINGS:
        greet_user()
    elif 'open' in command:
        if not open_website(command):
            speak("Sorry, I don't recognize that website.")
    else:
        # First try Wolfram Alpha
        if not wolfram_search(command):
            # If Wolfram can't answer, fallback to LLM
            ask_llm(command)
