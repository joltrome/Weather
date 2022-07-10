#! /usr/bin/env python3
from tkinter.tix import INTEGER
import requests
import json
import cgi

city_name = "Kyoto"
API_KEY = "d01ed74f13d285ba9f785fb49335bf3a"
API_KEY1 = "2cf78600fb5b485a87180ff28b4ddc06"

api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
api1= "https://timezone.abstractapi.com/v1/current_time/?api_key={key1}&location={city}"

form = cgi.FieldStorage()
city_name = form.getvalue('city','Kyoto')

url = api.format(city = city_name, key = API_KEY)
response = requests.get(url, "https://timezone.abstractapi.com/v1/current_time/?api_key=2cf78600fb5b485a87180ff28b4ddc06&location={city}")
data = response.json()
# jsonText = json.dumps(data, indent=4)

city = data["name"]
icon = data["weather"][0]["icon"]
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
timezone = data["timezone"]
latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]
feels = data["main"]["feels_like"]


print("Content-type: text/json\n")

weather = {"city": city, "icon": icon, "temp": temp, "humidity": humidity, "timezone": timezone,
"longitude": longitude, "latitude": latitude, "feels": feels}
print(json.dumps(weather))