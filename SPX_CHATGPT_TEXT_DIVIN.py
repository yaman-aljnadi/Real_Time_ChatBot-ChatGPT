import subprocess
import openai
import pyttsx3

import win32api
import win32gui
import time


openai.api_key = "INSERT TOKEN"
p = subprocess.Popen('spx recognize --microphone', stdout=subprocess.PIPE)

message_history = ''
engine = pyttsx3.init()

WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

hwnd_active = win32gui.GetForegroundWindow()

engine.startLoop(False)
while True:
    ## SPX Part from Azure you need to configure an Azure cognitive service in order to obtain a key and a region
    line = p.stdout.readline()
    line = line.strip().decode()
    print(line)
    if("RECOGNIZED:" in line):
        line = line.replace("RECOGNIZED: ", "")
        print(line)
        message_history = message_history + "\n" + line
        # print(message_history)
        response = openai.Completion.create(
            model = "text-davinci-003",
            temperature = 0.7,
            prompt = message_history,
            max_tokens=256
        )

        response = response.choices[0].text


        print(response)
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        time.sleep(0.3)
        engine.say(response)
        engine.iterate()
        time.sleep(0.3)
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)



            

        message_history = message_history + "\n" + response
        # print(message_history)



### A reminder for me win32api and win32gui are used to mute the microphone when listening.
### psyttsx3 is used as the audio output 
