import requests
from bs4 import BeautifulSoup

# Scrape weather information

def get_weather(location):
    # You need to replease `API_KEY` with your own Api_key from your account.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=API_KEY"
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    return f"Weather in {location}: {weather}\nTemperature: {temperature}°C"
    