import webbrowser
import os

def open_google():
    webbrowser.open('https://www.google.com/', new=2)

def open_facebook():
    webbrowser.open('https://www.facebook.com/', new=2)

def open_twitter():
    webbrowser.open('https://twitter.com/', new=2)

def open_youtube():
    webbrowser.open('/https://www.youtube.com/', new=2)

def close_browser():
    os.system("taskkill /im chrome.exe /f") 