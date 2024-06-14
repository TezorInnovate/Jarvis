import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import sys
import pywhatkit



engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(f"AI :{audio}")
    engine.runAndWait()

#speech to text
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(f"user :{query}")

    except Exception as e:
        speak("I didn't get that...")
        return "none"
    return query

#wish function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning sir")
    elif  hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("How can i help you")


if __name__ == "__main__":
    wish()
    while True:
    

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "  "
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "  "
            os.startfile(apath)

        elif "open command prompt" in query:
            os.startfile("  ")

        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results)

        elif "google" in query:
            speak("what would you like to search sir")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play" in query:
            play = query.replace("play ", "")
            speak("playing " + play)
            pywhatkit.playonyt(play)

        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(time)
            speak("current time is " + time)

        
        
        
        
        
        #terminate program
        elif "no" in query:
            speak("bye sir. going to sleep mode")
            sys.exit()

        speak("is there anything else i can help you with sir")



