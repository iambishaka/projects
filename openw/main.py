import requests

API_KEY = "838063b2c85e17f9e1c8d33b801ea4fe"

def get_current_wether(city_name, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
            "q" : city_name,
            "appid" : API_KEY,
            "units" : units
            }

    res = requests.get(url, params=params)

    print(res)

get_current_wether("Tokyo")

def coordinates(city_name):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
            "q"
            }
