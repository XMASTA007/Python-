from pyttsx3.engine import Engine
import speech_recognition as sr
import pyttsx3

import pywhatkit as pywk
import datetime
import wikipedia as wiki
import pyjokes


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


listener = sr.Recognizer()


def command_get():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "george" in command:
                command = command.replace('george', '')
    except:
        pass
    return command


def run_George():
    command = command_get()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        print('Playing: ' + song)
        pywk.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('Current time is ' + time)
    elif 'search' in command:
        try:
            queary = command.replace('search', '')
            info = wiki.summary(queary, 1)
            talk(info)
        except:
            talk('Nothing found on wikipedia for ' + info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
        print("Please say command again")

while True:
    run_George()
