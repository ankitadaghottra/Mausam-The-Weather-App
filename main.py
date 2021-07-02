from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(URL.format(city, api_key))
    if result:
        json = result.json()
        # (City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temperature_kelvin = json['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temperature_celsius, temperature_fahrenheit, icon, weather)
        return final
    else:
        return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = 'C:\\Users\\Dell\\PycharmProjects\\MausamTheWeatherApp\\weather_icons\\{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.2f} Degree Celsius, {:.2f} Degree Fahrenheit'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error', 'Cannot find the city {}'.format(city))


WeatherApp = Tk()
WeatherApp.title("Mausam: The Weather App!")
WeatherApp.geometry('700x350')
WeatherApp.config(bg = 'light blue')

city_text = StringVar()
city_entry = Entry(WeatherApp, textvariable=city_text)
city_entry.pack()

search_btn = Button(WeatherApp, text='Enter the City Name: ', width=15, command=search)
search_btn.pack()

location_lbl = Label(WeatherApp, text='', font=('bold', 20))
location_lbl.pack()

img = PhotoImage(file='')
Image = Label(WeatherApp, image=img)
Image.pack()

image = Label(WeatherApp, bitmap='')
image.pack()

temp_lbl = Label(WeatherApp, text='')
temp_lbl.pack()

weather_lbl = Label(WeatherApp, text='')
weather_lbl.pack()

WeatherApp.mainloop()
