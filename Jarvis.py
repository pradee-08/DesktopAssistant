import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good Morning Mr Reddy ")
    elif hour >=12 and hour < 18:
        speak("Good Evening Mr Reddy")
    
    speak("I'm Pallavi, how may I help you")


def takeCommand():
    '''
       Takes mic input from user and responds string output. 
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #Seconds of non speaking audio before a phrase is considered complete.
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("I didn't understand. Can you repeat it for me")
        return "None"
    return query




if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching Wikipedia")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\reddy\\OneDrive\\Desktop\\Dude\\Learning\\Python\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Mr Reddy, the time is {strTime}")
            speak(f"Mr Reddy, the time is {strTime}")

        elif 'open code' in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



