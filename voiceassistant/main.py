import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            # print('User said {}'.format(command))
            command=command.lower()
        return command

    except:
        pass
    
def run_alexa():
    talk('How can I help you?')
    command=take_command()
    print('Got command '+command)
    if 'play'in command:
        song=command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('The current time is ' + time)
    
    elif 'what is' in command:
        thing = command.replace('what is','')
        info=wikipedia.summary(thing)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is','')
        info=wikipedia.summary(person)
        talk(info)
    else:
        talk('I did not understand you.')
run_alexa()