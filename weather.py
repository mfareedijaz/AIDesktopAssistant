import requests, json
import math
from output_data import display_output


def weather(city):

    apikey = "ac349118659d1c1f2e6d75ca77f8e874"
    url = "https://api.openweathermap.org/data/2.5/weather?q="
    completeURL = url + city + "&units=metric" + "&appid=" + apikey
    response = requests.get(completeURL)
    data = response.json()
    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        speed = data['wind']['speed']
        weather = data['weather'][0]['main']
        display_output("Current Temperature: " + str(temp) + "C" )
        display_output("Weather: " + weather)
        display_output("Humidity: " + str(humidity) + "%")
        display_output("Speed: " + str(math.ceil(speed*3.6)) + "km/hr")
        return "Weather fetched successfully"
    else:
        return "Result not found!!!"