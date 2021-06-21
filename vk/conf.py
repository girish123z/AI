import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import psutil
import pyjokes

eng = pyttsx3.init()

def speak(cmd):
    eng.say(cmd)
    eng.runAndWait()

intro = """Hi My name is A I...
            I am an AI assistant.
            I am an ultimate creation of Vivek........................,
            Gourish ........................ And........... Sumeet.....................
            You can use me for doing several tasks for you"""

def Time():
    t = datetime.datetime.now().strftime("%I:%M %p")  # string format of time I=12 hour format p = am pm specification
    return t

def Greetings():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak("Good Morning, How can i help you today")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, How can i help you today")
    elif hour >= 18 and hour < 24:
        speak("Good Evening,, How can i help you today")
    else:
        speak("Good night, , How can i help you today")

def Take_Input():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening......")
        r.adjust_for_ambient_noise(src, 1)
        r.pause_threshold=1
        audio = r.listen(src) # waiting time for user to give the command
    try:
        print("recognizing.......")
        cmd = r.recognize_google(audio, language='en-US')
        print(cmd)
    except Exception as e:
        print(e)
        speak("Say that again")
        return "None"
    return cmd
