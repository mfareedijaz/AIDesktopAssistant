from time_module import get_time
from memory import get_AnsFromMemory
from output_data import display_output
from input_data import take_input
from memory import *
from browsers import *
from internet import checkInternet, checkOnWikipedia
import assistant_details
from whatsapp import *
import os
from brightness import *
from music import *
from wallpaper import changeBackground
from news import getLatestNews
from volume import volume
from close import close
from screenshot import ScreenShot
from weather import weather
from mouse import mouse
from remainder import about, notification
from battery import *
from search import *

def process_input(query):
    answer = get_AnsFromMemory(query)


    if (answer == "Get time details"):
        return ("Time is: "+ get_time())
    
    elif (answer == "on speak"):
        return turn_on_speech()
    
    elif (answer == "off speak"):
        return turn_off_speech()
    
    elif (answer == "open google"):
        open_google()
        return "opening google"

    elif (answer == "open facebook"):
        open_facebook()
        return "opening facebook"

    elif (answer == "open youtube"):
        open_youtube()
        return "opening youtube"

    elif (answer == "open twitter"):
        open_twitter()
        return "opening twitter"

    elif (answer == "close browser"):
        close_browser()
        return "closing browser"
    
    elif (answer == "screenshot"):
        ScreenShot()
        return "Task Terminated."

    elif (answer == "about"):
        about()
        return "Check the bottom right corner of your screen; a notification about us has popped up. Click here to learn more about the developer."
    
    elif (answer == "battery percentage"):
        display_output("Checking battery percentage... Please wait a while")
        sleep(2)
        return get_battery_percentage()
    
    elif (answer == "charging"):
        display_output("Checking plugged status... Please wait a while")
        sleep(2)
        return get_plugged_status()
    
    elif (answer == "remaindar"):
        display_output("Kindly provide the required details to configure a reminder.")
        display_output("Enter title: ")
        title = take_input()
        display_output("Enter message: ")
        msg = take_input()
        display_output("Enter duration(sec): ")
        duration = int(take_input())
        notification(title, msg, duration)
        return "The notification alert has been successfully configured in accordance with specified parameters."

    elif (answer == "open whatsapp"):
        display_output("Which function do you want to perform ?\n1. Send message on whatsapp\n2. Open specific chat")
        input = take_input()
        if input == '1':
            display_output("Please enter sender name: ")
            name = take_input()
            display_output("Enter message that you want to sent: ")
            message = take_input()
            display_output("Please wait")
            whatsappMessage(name, message)
            os.system("taskkill /im chrome.exe /f")
            return "Message sent successfully"
        elif input == '2':
            display_output("Please enter name to open his\her chat: ")
            name = take_input()
            whatsappChat(name)
            return "Chat opened successfully"
        else:
            return "invalid input!"

    elif (answer == "set brightness"):
        display_output("Enter brightness percentage that you want to set")
        set = int(take_input())
        get = setBrightness(set)
        return (f"Now brightness is set to {get}%")

    elif (answer == "youtube"):
        display_output("Opening youtube... Please wait a while")
        display_output("Enter here what you want to search on youtube: ")
        search = take_input()
        search_on_yt(search)
        return "Task terminated successfully"

    elif (answer == "open music player"):
        Music_Player()
        return "Task terminated successfully"
    
    elif (answer == "temperature" or answer == "weather"):
        # query = query.lower()
        # query = query.replace("tell me the temperature in", "")
        # query = query.replace("alexa tell me the temperature in", "")
        # query = query.replace("alexa tell me the weather in", "")
        # query = query.replace("give me the weather in", "")
        # query = query.replace("weather in", "")
        # query = query.replace("temperature in", "")
        # query = query.strip()
        display_output("Unlock the secrets of your city's weather with just a click – enter your city name and let the temperature unfold!")
        cityName = take_input()
        display_output("Fetching weather details.. Please wait a while")
        sleep(2)
        return weather(cityName)
    
    elif (answer == "close application"):
        return close()

    elif(answer == "check internet connection"):
        if (checkInternet()):
            return "Internet is connected"
        else:
            return "Internet is not connected"
    
    elif(answer == "virtual mouse"):
            display_output("Initializing virtual mouse... Please wait a while")
            sleep(2)
            mouse()
            return "Task terminated successfully"

    elif(answer == "change name"):
        display_output("Okay! What do you want to call me?")
        temp = take_input()
        if temp == assistant_details.name:
            return "Can't change. I think you are happy with my old name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "Now you can call me " + temp
        
    elif(answer == "change wallpaper"):
        display_output("Changing desktop background... Please wait a while")
        return changeBackground()
    
    elif(answer == "volume"):
        display_output("Initializing a webcam... Please wait a while")
        return volume()
    
    elif(answer == "news"):
        display_output("Fetching latest news.. Please wait a while")
        sleep(2)
        return getLatestNews()
    
    else:
        display_output("Don't know this one should i search on internet")
        ans = take_input()
        if "yes" in ans:
            answer = checkOnWikipedia(query)
            if (answer != ""):
                return answer
        else:   
            display_output("Can you please tell me what it means")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means","")
                ans = ans.strip()
                value = get_AnsFromMemory(ans)
                if (value == ""):
                    return "Can't help with this one"
                else:
                    insert_QuesAndAns(query, value)
                    return "Thanks I will remember it for the next time"
            else:
                return "Can't help with this one"