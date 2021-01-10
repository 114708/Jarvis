import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('now playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'Good news and bad news' in command:
        talk('Good news I have got you a woman, bad news she is american')
        # This is a quoted joke from a Twitch Streamer
    elif 'Jack Manifol?' in command:
        talk('Jack Mani-foll, Jack Mani-foll fall off bridge? Jack Mani fall of bridge. Jack Mani bye dudu du du')
        # This also is a quoted joke from a Twitch Streamer
    elif 'creeper' in command:
        talk('aww man')
    else:
        talk('Error. Please say the command again.')


while True:
    run_jarvis()
