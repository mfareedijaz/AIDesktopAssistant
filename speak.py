from gtts import gTTS
from playsound import playsound
import os
import winsound
def speak(text):
    tts = gTTS(text)
    tts.save('speech.mp3')
    winsound.PlaySound('speech.mp3',0)
    os.remove('speech.mp3')


speak("hello")