import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import datetime
import os
from pydub import AudioSegment
from pydub.playback import play
import pyautogui
wel =pyttsx3.init()
voices=wel.getProperty('voices')
wel.setProperty('voice',voices[0].id)
def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def takecommands():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say commands sear....')
        command.phrase_threshold=0.4
        audio=command.listen(mic)
        try:
            print('recordings...')
            query=command.recognize_google(audio,language='ar')
            print('you said:{query}')
        except Exception as Error:
                return None
music1=AudioSegment.from_mp3('C:\Users\pc.cc\Documents\ai using python\sounds\welcome.mp3')
play(music1)
while True:
    query=takecommands()

    if 'good mornings' in query:
        b=AudioSegment.from_mp3('sounds/goodmorning.mp3')
        play(b)
    if 'good evenings ' in query:
        b=AudioSegment.from_mp3('sounds/gooodevining.mp3')
        play(b)
    if 'opengoogle' in query:
        b=AudioSegment.from_mp3('sounds/google.mp3')
        play(b)
        time.sleep(2)
        webbrowser.open_new_tab('https://www.google.com')
    if 'whats i have to day' in query:
        b=AudioSegment.from_mp3('sounds/moa3d.mp3')
        play(b)
    if 'i want to programming a little' in query:
        b=AudioSegment.from_mp3('sounds/program.mp3')
        play(b)
    