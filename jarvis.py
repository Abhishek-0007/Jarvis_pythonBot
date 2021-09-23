from urllib.parse import quote
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import googlesearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir! ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir! ")
    else:
        speak("Good Evening Sir! ")

# speak("This is Jarvis, How can I help sir?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)
        print("Say the again please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'stop' in query:
            speak("Shutting Down")
            exit()

        elif 'time' in query:
            speak(datetime.time)
        
        elif 'open youtube' in query:
            speak("starting youtube")
            webbrowser.open("youtube.com")

        elif 'what is the meaning of' in query:
            query = query.replace("what is the meaning of", "")
            results = googlesearch.url_search_num(query)
            speak(results)
            

        
        
        
        
    