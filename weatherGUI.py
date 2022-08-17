import requests
from tkinter import *
import time

def weather_api():
    API_key = '070484f6d39ac688873359fc62a0ba3b'

    city = city_ent.get()

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + city
    weather_data = requests.get(base_url).json()

    # for key, value in weather_data.items():
    #     print(key, ":", value)

    root_ = Tk()
    root_.title("Weather")

    screen_width = root_.winfo_screenwidth()
    screen_height = root_.winfo_screenheight()

    x = int((screen_width / 2) - (900 / 2))
    y = int((screen_height / 2) - (365 / 2))

    root_.geometry("{}x{}+{}+{}".format(900, 365, x, y))

    Label(root_, text="Longitude : " + str(weather_data['coord']['lon']) + " °E", font=("Helvetica",14)).pack()
    Label(root_, text="Latitude : " + str(weather_data['coord']['lat']) + " °N", font=("Helvetica",14)).pack()
    Label(root_, text="Type : " + str(weather_data['weather'][0]['main']), font=("Helvetica",14)).pack()
    Label(root_, text="Temperature : " + str(round(weather_data['main']['temp']-273.15)) + " °C", font=("Helvetica",14)).pack()
    Label(root_, text="Feels like : " + str(round(weather_data['main']['feels_like'] - 273.15)) + " °C", font=("Helvetica",14)).pack()
    Label(root_, text="Minimum : " + str(round(weather_data['main']['temp_min'] - 273.15)) + " °C", font=("Helvetica",14)).pack()
    Label(root_, text="Maximum : " + str(round(weather_data['main']['temp_max'] - 273.15)) + " °C", font=("Helvetica",14)).pack()
    Label(root_, text="Pressure : " + str(weather_data['main']['pressure']) + " hPa", font=("Helvetica",14)).pack()
    Label(root_, text="Humidity : " + str(weather_data['main']['humidity']) + " %", font=("Helvetica",14)).pack()
    Label(root_, text="Visibility : " + str(weather_data['visibility']/1000) + " km", font=("Helvetica",14)).pack()
    Label(root_, text="Wind Speed : " + str(weather_data['wind']['speed']) + " m/s", font=("Helvetica",14)).pack()
    Label(root_, text="Sunrise : " + time.strftime('%I:%M:%S %p', time.localtime(weather_data['sys']['sunrise'])), font=("Helvetica", 14)).pack()
    Label(root_, text="Sunset : " + time.strftime('%I:%M:%S %p', time.localtime(weather_data['sys']['sunset'])), font=("Helvetica", 14)).pack()

root = Tk()
root.title("Weather")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (450 / 2))
y = int((screen_height / 2) - (250 / 2))

root.geometry("{}x{}+{}+{}".format(450, 250, x, y))

city_lbl = Label(root, text="Enter City Name", font=("Helvetica",30))
city_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)
city_ent = Entry(root, font=("Helvetica",14))
city_ent.place(relx=0.5, rely=0.5, anchor=CENTER)
search_btn = Button(root, text="Search", font=("Helvetica",10), command=weather_api, bg="yellow", foreground="red", activebackground="red", activeforeground="yellow")
search_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

root.mainloop()