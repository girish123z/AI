from flask import Flask, render_template,request,redirect,url_for,session,logging
import main
import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import psutil
import pyjokes
import os
import pywhatkit
import wikipedia
import webbrowser as wb
from gtts import gTTS
from playsound import playsound
import os

app = Flask(__name__)




def speek(txts):
    tts = gTTS(text=txts, lang='en',slow=False)
    tts.save("good.mp3")
    playsound('C://Users//User//Desktop//vk//good.mp3')
    os.remove('C://Users//User//Desktop//vk//good.mp3')

intro = """Hi My name is A I,
            I am an AI assistant.
            I am an ultimate creation of Vivek,
            You can use me for doing several tasks for you"""

def Time():
    t = datetime.datetime.now().strftime("%I:%M %p")  # string format of time I=12 hour format p = am pm specification
    return t

def Greetings():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speek("Good Morning, How can i help you today")
    elif hour >= 12 and hour < 18:
        speek("Good Afternoon, How can i help you today")
    elif hour >= 18 and hour < 24:
        speek("Good Evening,, How can i help you today")
    else:
        speek("Good night, , How can i help you today")

def Take_Input():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening......")
        res="Listening..."
        r.adjust_for_ambient_noise(src, 1)
        r.pause_threshold=1
        audio = r.listen(src) # waiting time for user to give the command
    try:
        print("recognizing.......")
        res="Recognizing..."
        cmd = r.recognize_google(audio, language='en-US')
        print(cmd)
    except Exception as e:
        print(e)
        speek("Say that again")
        return "None"
    return cmd


@app.route("/",methods=['GET','POST'])
def index():
    txts="..."
    if request.method=="POST":
        Greetings()
        while True:
            cmd = Take_Input().lower()
            if "yourself" in cmd:
                speek(intro)
                return render_template("index.html",cmd=intro)
            elif "time" in cmd:
                t = Time()
                speek("current time is "+t)
                tim="current time is "+t
                return render_template("index.html",cmd=tim)
            elif "go to sleep" in cmd:
                speek("Ok as your wish, Have a nice day Good Bye")
                break
                return render_template("index.html")
            else:
                speek("Can you please give me a valid command")
    return render_template("index.html")



if __name__ == '__main__':
    app.run()
