from os import startfile
from pyautogui import click
from keyboard import press, write
from time import sleep

def whatsappMessage(name, message):
    startfile("https://web.whatsapp.com/")
    sleep(25)
    click(x=138, y=164)
    sleep(1)
    write(name)
    sleep(1)
    click(x=199, y=282)
    sleep(1)
    click(x=630, y=713)
    sleep(1)
    write(message)
    press('enter')
    sleep(5)

# whatsappMessage('mama','hello')

def whatsappChat(name):
    startfile("https://web.whatsapp.com/")
    sleep(55)
    click(x=138, y=164)
    sleep(1)
    write(name)
    sleep(1)
    click(x=199, y=282)
    sleep(1)