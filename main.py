import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes




listener= sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():

    try:
          with sr.Microphone() as source:
              print("listening...")
              voice = listener.listen(source)
              command = listener.recognize_google(voice)
              command = command.lower()
              if 'alexa' in command:
                  command = command.replace('alexa','')



    except:
        pass
    return  command




def run_alexa():
    command = take_command()
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about' , '')
        info = wikipedia.summary(look_for,3)
        talk(info)
    elif 'jokes' in command:
        talk(pyjokes.get_jokes())
    elif 'date' in command:
        talk('sorry vaiya, you are not my type')
    else:
        talk('come again! or i can search it on google')
        pywhatkit.search(command)






while True:
    run_alexa()
