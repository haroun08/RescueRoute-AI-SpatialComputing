import requests

def fetch_traffic_data(api_key):
    url = f"https://api.traffic.com/data?key={api_key}"
    response = requests.get(url)
    return response.json()

def fetch_weather_data(api_key):
    url = f"https://api.weather.com/data?key={api_key}"
    response = requests.get(url)
    return response.json()