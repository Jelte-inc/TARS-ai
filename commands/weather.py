import requests
import os

url = "http://api.weatherapi.com/v1/forecast.json"  

location = ""

while True:
    location = input()

    params = {
        "key": os.getenv("KEY"),
        "q": location,  
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data['current']['temp_c']  
        precip = data['current']['precip_mm']  
        print(f"Temperatuur: {temp}°C")
        print(f"Neerslag: {precip} mm")
    else:
        print(f"Fout: {response.status_code}, {response.json().get('error', {}).get('message', 'Onbekende fout')}")