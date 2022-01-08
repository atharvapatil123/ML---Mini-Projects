import speech_recognition as sr
import pyttsx3 # Python test-to-speech version 3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch
import webbrowser
import time
import python_weather
import python_weather
import asyncio



listener = sr.Recognizer()
engine = pyttsx3.init() # Initializing text-to-speech package
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[2].id) # Setting voice as female tone, voices has all voice options


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source) # Recognizes your voice
            command = listener.recognize_google(voice) # Converts to text
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command)
    except:
        pass
    return command

async def find_weather(place):
    client = python_weather.Client()
    weather = await client.find(place)
    print(weather)
    print()
    talk(f'Temperature in {place} is {weather.current.temperature} degrees celcius')
    print(f'Temperature in {place} is {weather.current.temperature} degrees celcius')
    print()
    print('Next few days weather forecasts: \n')
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)
    print()
    webbrowser.open(weather.url)
    time.sleep(5)
    await client.close()


def run_alexa(command):
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'weather' in command:
        last = command.rfind(' ')
        place = command[last+1:]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(find_weather(place))
        # print(com) 

    elif 'whatsapp' in command or 'message' in command:
        talk('Whom you want me to message on whatsapp?')
        print()
        print('Whom you want me to message on whatsapp?')
        try:
            with sr.Microphone() as source2:
                while(True):
                    print('listening...')
                    voice2 = listener.listen(source2) # Recognizes your voice
                    number = listener.recognize_google(voice2) # Converts to text
                    number = number.lower()
                    time.sleep(3)

                    talk("Is this number correct: ",number)
                    ans = input("Is this number correct: ",number," Y/n")
                    if ans == "Y" or ans == "y":
                        break
                    else :
                        continue
        except:
            pass

        talk('What is the message?')
        print()
        print('What is the message?')
        try:
            with sr.Microphone() as source3:
                print('listening...')
                voice2 = listener.listen(source3) # Recognizes your voice
                message = listener.recognize_google(voice2) # Converts to text
                message = message.lower()
                print(message)
        except:
            pass

        talk('At what time you want me the message to be sent? In 24-hour format.')
        talk('Tell me the hour at which the message must be sent?')
        print()
        print('Tell me the hour at which the message must be sent?')
        try:
            with sr.Microphone() as source4:
                print('listening...')
                voice4 = listener.listen(source4) # Recognizes your voice
                hour = listener.recognize_google(voice4) # Converts to text
                hour = hour.lower()
                hour = int(hour)
                print(hour)
        except:
            pass

        talk('Tell me the minute at which the message must be sent?')
        print()
        print('Tell me the minute at which the message must be sent?')
        try:
            with sr.Microphone() as source5:
                print('listening...')
                voice5 = listener.listen(source5) # Recognizes your voice
                minute = listener.recognize_google(voice5) # Converts to text
                minute = minute.lower()
                minute = int(minute)
                print(minute)
        except:
            pass
        talk(f'Message will be delivered to ${number}. Message is ${message}, and will be sent at ${hour} hrs ${minute} minutes')
        pywhatkit.sendwhatmsg(number, message, hour, minute, 32)


    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time_now)
        talk('Current time is ' + time_now)

    elif 'date' in command:
        date = datetime.date.isoformat(datetime.date.today())
        print("Today's date is "+ date)
        talk("Today's date is "+ date)

    elif 'who the heck is'  in command or 'who is'  in command or 'search for' in command or 'wikipedia' in command:
            if 'who the heck is' in command:
                person = command.replace('who the heck is', '')
            if 'who is' in command:
                person = command.replace('who is', '')
            if 'search for' in command:
                person = command.replace('search for', '')
            if 'summary' in command:
                person = command.replace('search for', '')

            talk(f'These are the results for {person} on google')
            res = googlesearch.search(person, num_results=10)
            print(res)
            webbrowser.open(res[0])

    elif 'a date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('No, I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        if('quit' in command) or ('stop' in command):
            pass
        else:    
            talk('Please say the command again.')
    
    time.sleep(5)

print(
    ''' Hey, Welcome to my talking chatbot. 
    I was always curious of developing something like this and 
    finally I have completed it. 
    '''
)

while True:
    command = take_command()
    print(command)
    run_alexa(command)
    if ('stop'  in command) or ('quit' in command):
        talk('It was a nice experience talking with you. Hope to talk with you again!')
        break