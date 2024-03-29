import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
#sapy5 is microsoft voice recognition API
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hey riya, how can i help you today")

def takecommand():
    # it takes a microphone input from the user and returns string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query= r.recognize_google(audio,language='en-in')
        print("user said:", query)
    except Exception as e:
        #print(e)
        speak("say that again please.......")
        return "none"
    return query


if __name__=='__main__':
    wishme(datetime)
    while True:
    # if 1:
            query = takecommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif "open youtube " in query:
                webbrowser.open("youtube.com")

            elif "open google " in query:
                webbrowser.open("google.com")

            elif "open notepad" in query:
                osCommandString = "notepad.exe file.txt"
                os.system(osCommandString)
                
            elif 'open command prompt' in query:
                os.system('start cmd')

            elif 'open stackflow' in query:
                webbrowser.open('stackoverflow.com')

            elif 'open calender' in query:
                webbrowser.open('calendar.google.com')

            elif 'time ' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'no thanks' in query:
                speak(" thank you for using me. have a good day")
                sys.exit()
