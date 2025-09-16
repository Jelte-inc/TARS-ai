import requests

location = input()

api_url = f'http://api.weatherapi.com/v1/current.json?key=4b67ad035fab4203ac3114208251609&q={location}&aqi=no'

response = requests.get(api_url)
print("hello")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    data = response.json
    print(response.status_code)
    print(data)
