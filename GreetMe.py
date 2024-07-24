import pyttsx3
import speech_recognition
import datetime
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")  
engine.setProperty("voice",voices[0].id) #here i used mic david 
#print(voices[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,mam")
    elif hour>12 and hour<=18:
        speak("Good Afternoon ,mam")
    else:
        speak("Good Evening,mam")
    speak("Please tell me, How can I help you ?")


