import requests
import os
from dotenv import load_dotenv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def weather_forcast(user_input:str):
    url = "http://api.weatherapi.com/v1/forecast.json"  
    load_dotenv()
    key = os.getenv("API_KEY")

    if key is None:
        print("Api key is missing")

    location = user_input
    days_input = input('for when do you want to know the weather? (input in days from today, so today is 0) ')

    possible_inputs = {'today': 0, 'tomorrow': 1}
    best_match, score = process.extractOne(days_input, possible_inputs.keys(), scorer=fuzz.ratio, score_cutoff=50)

    if best_match is None:
        print('best match is None')
    else:
        days = possible_inputs[best_match]
        print(days)

    params = {
        "key": key,
        "days": days,
        "q":location
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']  
        precip = data['current']['precip_mm']  
        print(f"Temperature: {temp}°C")
        print(f"Rain: {precip} mm")
    else:
        print(f"Fout: {response.status_code}, {response.json().get('error', {}).get('message', 'Unknown error')}")