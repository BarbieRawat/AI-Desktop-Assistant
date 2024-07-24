import pyttsx3  #to make jarvis speak
import speech_recognition
import os
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")  
engine.setProperty("voice",voices[0].id) #here i used mic david 
#print(voices[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=300  #it should be handled carefully to listen to our pitch
        audio=r.listen(source,0,4) #wait for 4 sec and then move ahead
    try:
        print("Understanding....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    
    except Exception as e:
        print("Say that again")
        return "None"
    return query 
    
if __name__ =="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query=takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok mam ,You can call me any time")
                    break
                elif "hello" in query:
                    speak("Hello mam, How are you?")
                elif "i am fine" in query:
                    speak("that's great mam")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("your welcome sir")
                elif "internet speed" in query:
                    import speedtest
                    wifi=speedtest.Speedtest()
                    upload_net=wifi.upload()/1048576 #1megab=1024*1024bytes
                    download_net=wifi.download()/1048576
                    print("wifi upload speed is",upload_net)
                    print("wifi download speed is",download_net)
                    speak(f"wifi download speed is {download_net}")
                    speak(f"wifi upload speed is {upload_net}")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown=input("Do you wish to shutdown you computer?(yes/no)")
                    if shutdown=="yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown =="no":
                        break
                    



                

