import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
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

query=takeCommand().lower()
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")  
engine.setProperty("voice",voices[0].id) #here i used mic david 
#print(voices[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query=query.replace("jarvis","")
        query=query.replace("google search","")
        query=query.replace("google","")
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)
        except:
            print("done")
def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search")
        query=query.replace("youtube search","")
        query=query.replace("youtube","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query) #open 1st vedio
        speak("Done,mam")
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query=query.replace("wikipedia","")
        query=query.replace("search wikipedia","")
        results=wikipedia.summary(query,sentences=2) #fetching 2 sentences
        speak("According to wikipedia...")
        print(results)
        speak(results)



    
