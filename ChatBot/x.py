# from googlesearch import search
# print(search("Google"))

# import webbrowser
# # webbrowser.open('http://www.python.org')
# import python_weather
# import asyncio

# async def find_weather():
#     client = python_weather.Client()
#     weather = await client.find("Delhi")
#     print("abcd",weather)
#     webbrowser.open(weather.url)
#     await client.close()

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(find_weather())

# command = "I was always curious of developing something like this and"
# last = command.rfind(' ')
# com = command[last+1:]
# print(com) 

import pywhatkit
pywhatkit.sendwhatmsg('Sahil Kedare', 'Hi, This is Atharva. This message is sent using pywhatkit package of python. See here https://www.geeksforgeeks.org/introduction-to-pywhatkit-module/', 17, 57, 32)