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
from GoogleNews import GoogleNews
import howdoi
import os

listener = sr.Recognizer()
engine = pyttsx3.init() # Initializing text-to-speech package
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id) # Setting voice as female tone, voices has all voice options


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
            if 'arno' in command:
                command = command.replace('arno', '')
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


def run_arno(command):

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)            
        time.sleep(5)

    elif 'weather' in command:
        last = command.rfind(' ')
        place = command[last+1:]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(find_weather(place))
        time.sleep(5)
        # print(com) 

    elif 'news' in command:
        talk('Just tell me the topic on which you want the news?')
        print()
        print('Just tell me the topic on which you want the news?')
        with sr.Microphone() as source9:
            voice9 = listener.listen(source9)
            val = listener.recognize_google(voice9) 
            print(val)
            googlenews = GoogleNews()
            googlenews.set_lang('en')
            googlenews.set_period('7d')
            googlenews.set_encode('utf-8')
            googlenews.get_news(val)
            googlenews.results(sort=True)
            talk('These are the top 5 results for your search')
            print()
            print('These are the top 5 results for your search')
            ans5 = googlenews.get_texts()
            top5 = ans5[:5]
            for news in top5:
                print(news)
                talk(news)

    elif 'how do i' in command:
        command = command.replace('how do i', '')
        os.system(f'howdoi {command}')
        talk('The result is displayed in the terminal')
        # pywhatkit.playonyt(song)            
        time.sleep(15)

    elif 'whatsapp' in command or 'message' in command:
        try:
            with sr.Microphone() as source2:
                while(True):
                    talk('Whom you want me to message on whatsapp? Tell me the number with country code')
                    print()
                    print('Whom you want me to message on whatsapp? Tell me the number with country code')                   
                    print('listening...')
                    voice2 = listener.listen(source2) # Recognizes your voice
                    number = listener.recognize_google(voice2) # Converts to text
                    number = number.lower()

                    talk("Is this number correct: ")
                    talk(number)
                    print()
                    print("Is this number correct: ", number)

                    with sr.Microphone() as source6:
                        voice6 = listener.listen(source6)
                        ans1 = listener.recognize_google(voice6) 
                        print(ans1)
                        time.sleep(3)
                        if "Yes" in ans1 or "yes" in ans1 or'yeah' in ans1 or 'Yeah' in ans1:
                            break
                        else :
                            continue
        except:
            pass

        try:
            with sr.Microphone() as source3:
                while(True):
                    talk('What is the message?')
                    print()
                    print('What is the message?')
                    print('listening...')
                    voice2 = listener.listen(source3) # Recognizes your voice
                    message = listener.recognize_google(voice2) # Converts to text
                    message = message.lower()

                    talk("Is this message correct: ")
                    talk(message)
                    print()
                    print("Is this message correct: ", message)

                    with sr.Microphone() as source7:
                        voice7 = listener.listen(source7)
                        ans2 = listener.recognize_google(voice7) 
                        print(ans2)
                        time.sleep(3)
                        if "Yes" in ans2 or "yes" in ans2 or'yeah' in ans2 or 'Yeah' in ans2:
                            break
                        else :
                            continue
        except:
            pass

        talk('At what time you want me the message to be sent? In 24-hour format.')
        try:
            with sr.Microphone() as source4:
                while(True):
                    talk('Tell me the hour at which the message must be sent?')
                    print()
                    print('Tell me the hour at which the message must be sent?')
                    print('listening...')
                    voice4 = listener.listen(source4) # Recognizes your voice
                    hour = listener.recognize_google(voice4) # Converts to text
                    hour = hour.lower()
                    if hour.isdigit():
                        hour = int(hour)
                        talk("Is this value of hour correct: ")
                        talk(hour)
                        print()
                        print("Is this value of hour correct: ", hour)
                        
                    else:
                        talk("Please provide integer value of hour")
                        print()
                        print("Please provide integer value of hour: ", hour)
                        continue

                    with sr.Microphone() as source8:
                        voice8 = listener.listen(source8)
                        ans3 = listener.recognize_google(voice8) 
                        print(ans3)
                        time.sleep(3)
                        if "Yes" in ans3 or "yes" in ans3 or'yeah' in ans3 or 'Yeah' in ans3:
                            break
                        else :
                            continue
        except:
            pass

        try:
            with sr.Microphone() as source5:
                while(True):
                    talk('Tell me the minute at which the message must be sent?')
                    print()
                    print('Tell me the minute at which the message must be sent?')
                    print('listening...')
                    voice5 = listener.listen(source5) # Recognizes your voice
                    minute = listener.recognize_google(voice5) # Converts to text
                    minute = minute.lower()
                    if minute.isdigit():
                        minute = int(minute)
                        talk("Is this value of minute correct: ")
                        talk(minute)
                        print()
                        print("Is this value of minute correct: ", minute)
                    else:
                        talk("Please provide integer value of minute")
                        print()
                        print("Please provide integer value of minute: ", minute)
                        continue

                    
                    with sr.Microphone() as source9:
                        voice9 = listener.listen(source9)
                        ans4 = listener.recognize_google(voice9) 
                        print(ans4)
                        time.sleep(3)
                        if "Yes" in ans4 or "yes" in ans4 or'yeah' in ans4 or 'Yeah' in ans4:
                            break
                        else :
                            continue
        except:
            pass

        if(number=='' or str(hour)=='' or str(minute)=='' or message==''):
            talk('Message could not be sent')
            print('Message could not be sent')
            print()
        else:
            talk('Message will be delivered to ')
            talk(number)
            talk(' at ')
            talk(hour)
            talk(' hours ')
            talk(minute)
            talk(' minutes')
            print()
            print('Message will be delivered to ', number,' at ', hour,' hrs ', minute,' minutes\n')
            pywhatkit.sendwhatmsg(number, message, hour, minute, 40)
            time.sleep(10)



    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time_now)
        talk('Current time is ' + time_now)

    elif 'date' in command:
        date = datetime.date.isoformat(datetime.date.today())
        print("Today's date is "+ date)
        talk("Today's date is "+ date)

    elif 'who the heck is'  in command or 'who is' in command or 'search for' in command or 'wikipedia' in command or 'what is' in command or 'where is' in command or 'summary' in command :
            person = command
            if 'who the heck is' in command:
                person = command.replace('who the heck is', '')
            if 'who is' in command:
                person = command.replace('who is', '')
            if 'search for' in command:
                person = command.replace('search for', '')
            if 'summary' in command:
                person = command.replace('summary', '')

            talk(f'These are the results for {person} on google')
            res = googlesearch.search(person, num_results=10)
            print(res)
            webbrowser.open(res[0])
            time.sleep(5)


    elif 'a date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('No, I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        if(command!='' and (('quit' in command) or ('stop' in command) or ('exit' in command) or ('thank you' in command) or ('thanks' in command))):
            pass
        else:    
            talk('Please say the command again.')


talk(''' Welcome!! My name is Arno and I am your talking chatbot.
    I am developed by Atharva and he is my friend.
    I am curious and excited to answer your questions. 
    Feel free to ask me some questions.
    ''')
print(
    ''' Welcome!! My name is Arno and I am your talking chatbot. 
    I am developed by Atharva and he is my friend.
    I am curious and excited to answer your questions. 
    Feel free to ask me some questions.
    '''
)

while True:
    command = take_command()
    print(command)
    run_arno(command)
    if ('stop'  in command) or ('quit' in command) or ('exit' in command) or ('thank you' in command) or ('thanks' in command):
        talk('It was a nice experience talking with you. Hope to talk with you again!')
        break