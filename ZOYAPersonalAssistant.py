#package for speech_recognition
import speech_recognition as sr

#package for text-to-speech
import pyttsx3

#package for random response
import random

#package for webbrowser
import webbrowser
import wikipedia
import requests
from googlesearch import search

#greetings and response array
greetings=["hello how are you","how are you doing","Hey","what's up dude","Hello"]
response=["i am fine dood","i'm so cool, how about you","i'm fine","hey there,i am fine, what you doing"]
l1=["Instagram","Twitter","Facebook","FB","Wikipedia","Google"]
l2=["www.instagram.com","www.twitter.com","www.facebook.com","www.facebook.com","www.wikipedia.org","www.google.com"]
#welcome
def welcome():
   engine.say("hello How can i help you")
   engine.runAndWait()


#greetingfunction
def greeting():
     engine.say(random.choice(["i am fine dood","i'm so cool, how about you","i'm fine","hey there,i am fine, what you doing"]))
     engine.runAndWait()
     

#openapp function
def openApp(text):
  for i in range(len(l1)):
     if l1[i] in text:
        engine.say("opening"+l1[i])
        engine.runAndWait()
        webbrowser.open_new_tab("http://"+l2[i])
        break

#search function
def searchweb(text):
   searchresults=wikipedia.search(text)
   if not searchresults:
      engine.say("NO results")
      engine.runAndWait()
      return
   else:
     try:
       page=wikipedia.page(searchresults[0])
       engine.say("Here is what i have found for you")
     except Exception as err:
       page=wikipedia.page(err.options[0])
     
     engine.say(wikipedia.summary(text))
     engine.runAndWait()
   engine.say("Was it satisfying")
   r=sr.Recognizer()
   with sr.Microphone() as source:
    audio=r.listen(source) 
    try:
      text1=r.recognize_google(audio)
      if 'no' in text1:
          googlesearch(text) 
    except Exception as e:
          engine.say("Try saying it again") 


#googlesearch
def googlesearch(text):
   webbrowser.open_new_tab("www.google.com/search?q="+text)
#initialize microphone
mic_name="Microphone(Realtek(R) Audio)"

sample_rate=48000
chunk_size=2048
r=sr.Recognizer()
engine=pyttsx3.init()

engine.setProperty('rate',150)
#initialize device_id to microphone 
device_id=0
mic_list=sr.Microphone.list_microphone_names()
for i,microphone_name in enumerate(mic_list):
    if microphone_name==mic_name:
       device_id=i

with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size) as source:
     r.adjust_for_ambient_noise(source)
     while(True):
         welcome()
         #listening audio from user
         audio=r.listen(source)
         #convert audio to text and initialize it to text
         try:
           text=r.recognize_google(audio)
           print(text)
           #call greetings function
           if text in greetings:
              greeting()
           elif 'open' in text:
              openApp(text)
               
           else:
              searchweb(text)
         
         except Exception as e:
           engine.say("Sorry I am unable to understand you")
           engine.runAndWait()
           pass

