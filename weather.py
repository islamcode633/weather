import requests
import json
from pprint import pprint

# token -> config.file 
API_KEY = '197fd9986654de05a43c223870361230'


def get_info_about_weather(city: str = ""):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url=URL)
        pprint(response.content)
    except Exception as e:
        print(e)


get_info_about_weather(city=input())
