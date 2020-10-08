import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

print("ho rha hu start ruk ja")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    speak("good")

speak("Maynk mere lode pr")