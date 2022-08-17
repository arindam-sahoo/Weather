import requests
# Requests is a Python Library to send request to any website. This is an API, so we have to send request. So this is the way.
from pprint import pprint
import time
# When we send a request to the website it returns the data in JSON format which is not easy for print() function to visualize or print, thats why we use pprint.
# It will turn the JSON format into a tree which can be read normally.

API_key = '070484f6d39ac688873359fc62a0ba3b'

city = input("Enter a city : ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city
weather_data = requests.get(base_url).json()

pprint(weather_data)

print("Longitude : " + str(weather_data['coord']['lon']) + " °E")
print("Latitude : " + str(weather_data['coord']['lat']) + " °N")
print("Type : " + str(weather_data['weather'][0]['main']))
print("Temperature : " + str(round(weather_data['main']['temp']-273.15)) + " °C")
print("Feels like : " + str(round(weather_data['main']['feels_like'] - 273.15)) + " °C")
print("Minimum : " + str(round(weather_data['main']['temp_min'] - 273.15)) + " °C")
print("Maximum : " + str(round(weather_data['main']['temp_max'] - 273.15)) + " °C")
print("Pressure : " + str(weather_data['main']['pressure']) + " hPa")
print("Humidity : " + str(weather_data['main']['humidity']) + " %")
print("Visibility : " + str(weather_data['visibility']/1000) + " km")
print("Wind Speed : " + str(weather_data['wind']['speed']) + " m/s")
print("Sunrise : " + time.strftime('%I:%M:%S %p', time.localtime(weather_data['sys']['sunrise'])))
print("Sunset : " + time.strftime('%I:%M:%S %p', time.localtime(weather_data['sys']['sunset'])))