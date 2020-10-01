import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
from time import ctime
import pywhatkit as kit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print (voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("good morning shakthi")
    elif hour>=12 and hour<17:
        speak("good afternoon shakthi raj")  
    elif hour>=17 and hour<21:
        speak("good evening shakthi")   
    # else:
        # speak("good night shakthi")

    speak("i am maria, how may i help you ?")

def TakeCommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print(e)
        print("voice is not recognized, please try again..")
        speak("voice is not recognized, please try again..") 
        return "None"
    return query    


if __name__ == "__main__":
    wishMe()
    while True:
            query = TakeCommmand().lower()
            if 'wikipedia' and 'who is' in query:
                speak("searching wikipedia..")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=1)
                speak("according to wikipedia")
                print(results)
                speak(results)

            elif 'trending on youtube' in query:
                webbrowser.open("https://www.youtube.com/feed/trending")

            elif 'play' in query:
                kit.playonyt(query)
                # webbrowser.open(f"https://www.youtube.com/results?search_query={query}\n")
                speak("here is what i found for" + query)

            elif 'search' in query:
                speak("what do you want to search ?")
                search = TakeCommmand()
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                speak("here is what i found for" + search)
            elif 'vs code' in query:
                codepath = "M:\\Microsoft VS Code\\Code.exe"    
                speak("opening vs code")
                os.startfile(codepath)
            
            elif 'pubg' in query:
                codepath = "C:\\Program Files\\TxGameAssistant\\AppMarket\\AppMarket.exe" 
                speak("opening pubgee..")
                os.startfile(codepath) 
            elif 'html helper' in query:
                webbrowser.open("https://devdocs.io/")
                speak("here is what i found for" + query) 

                
            elif 'time' in query:
                print(ctime())
                speak(ctime())   
            
                
            elif 'exit' in query:
                hour = (datetime.datetime.now().hour)
                if hour>=6 and hour<22:
                    speak("ok sir.....have a good day..")
                    exit()
                else:
                    speak("ok sir...good night..")
                    exit()
    
       

    