import datetime as dt

import requests # pip install requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = "8cf4d5f176b85f669462549636b2d8e3"

CITY = "London"



url = BASE_URL + "appid="+ API_KEY + "&q=" + CITY


response = requests.get(url).json()


def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) +32
    return celsius, farenheit

temp_kelvin = response['main']['temp']
temp_celsius , temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response[response['sys']['sunrise'] + response['timezone']])
sunset_time = dt.datetime.utcfromtimestamp(response[response['sys']['sunset'] + response['timezone']])


print(f"Temperature in {CITY} : {}")





print(response)


