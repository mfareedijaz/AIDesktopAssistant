from os import startfile
from pyautogui import click
from keyboard import press, write
from time import sleep
from mouse import mouse
from remainder import notification

def search_on_yt(search):
    startfile("https://www.youtube.com/")
    sleep(15)
    click(x=704, y=108)
    sleep(2)
    write(search)
    sleep(2)
    click(x=922, y=110)
    notification("ALERT", "Enabling virtual mouse...", 2)
    mouse()