import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("City? ")

params = {
        'q': city,
        'units': 'metric',
        'appid': '11c0d3dc6093f7442898ee49d2430d20'
        }
res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json())
data = res.json()
#print(data["main"]["temp"])
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))
