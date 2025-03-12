# speech_utils.py

import pyttsx3
import speech_recognition as sr
from constants import MIC_NAME, SAMPLE_RATE, CHUNK_SIZE

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    device_id = None
    mic_list = sr.Microphone.list_microphone_names()
    
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == MIC_NAME:
            device_id = i
            break
            
    with sr.Microphone(device_index=device_id, sample_rate=SAMPLE_RATE, chunk_size=CHUNK_SIZE) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except:
            speak("Sorry, I couldn't understand you.")
            return None
