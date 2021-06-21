from conf import *
import os
import pywhatkit
import wikipedia
import webbrowser as wb

def voice():
    Greetings()
    while True:
        cmd = Take_Input().lower()
        # if "hello" or "hi" in cmd:
        #     speak("Hello dear")

        if "yourself" in cmd:
            speak(intro)

        elif "time" in cmd:
            t = Time()
            speak("current time is "+t)


        #..................................................................................................................

        elif "go to sleep" in cmd:
            speak("Ok as your wish. Have a nice day Good bye!!")
            break

        else:
            speak("Can you please give me a valid command")
