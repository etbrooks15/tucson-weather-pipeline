'''This program extracts information about Tucson's weather.'''
import requests

def extract_weather_data():
    '''This function extracts weather data for Tucson from the Open-Meteo API.'''
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=32.22&longitude=-110.97&start_date=2026-06-01&end_date=2026-08-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America/Phoenix"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


weather_data = extract_weather_data()
dates = weather_data["daily"]["time"]
highs = weather_data["daily"]["temperature_2m_max"]

for date, high in zip(dates, highs):
    print(f"{date}: {high}")
    
