import requests
import os
from dotenv import load_dotenv

url = "http://api.weatherapi.com/v1/forecast.json"  

location = ""

load_dotenv()

key = os.getenv("API_KEY")

while True:
    location = input()

    days = input('for when do you want to know the weather? (input in days from today, so tomorrow is 1)' )

    params = {
        "key": key,
        "q": location,  
        "days": days
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        temp = data['current']['temp_c']  
        precip = data['current']['precip_mm']  
        print(f"Temperature: {temp}°C")
        print(f"Rain: {precip} mm")
    else:
        print(f"Fout: {response.status_code}, {response.json().get('error', {}).get('message', 'Unknown error')}")