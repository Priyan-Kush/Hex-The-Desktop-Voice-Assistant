import queue
from unittest import result
from winreg import QueryValue
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
voices= engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print('Good Morning! Hex here')
    elif hour>=12 and hour<18:
        print('Good Afternoon Hex here!')

    else:
        speak('Good Evening! Hex here')
    
    speak('I am here to help you')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('priyankushk29@gmail.com', to, content)
    server.close()



if __name__ == '__main__':
    wishMe()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query= query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open YouTube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open Google' in query:
            webbrowser.open('google.com')
        
        elif 'open StackOverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        # elif 'play music' in query:
        #     music_dir= 'C:\Users\\KIIT\\Downloads\\Music'
        #     songs=  os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The Time is {strTime}')
        
        # elif 'Open VS Code' in query:
        #     Codepath ="C:\Users\KIIT\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile(Codepath)
        
        elif 'Email to Kush' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to = 'priyankushk29@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(" Sorry the email couldnt be sent Kush")

                