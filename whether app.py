import requests
import json
city = input("Enter the city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=b71b9533b87d4794a6752930231110&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic)
print(wdic["current"]["temp_c"])
print(wdic["location"]["localtime"])