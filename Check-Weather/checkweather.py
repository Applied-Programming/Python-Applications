#! Python 3.4
# checkweather.py - Prints the current weather for a location from the command line.


import json
import requests
import sys

#app_ID = 'YOUR-OWN-OPENWEATHERMAP-API'
location = ('Nagpur,IN')

# Download the JSON data from OpenWeatherMap.org's API using the Python requests module
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, app_ID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data.
weather_data = json.loads(response.text)

# Print weather descriptions:
w = weather_data['weather']

print('Current weather in %s:' % (location))
print(w[0]['main'], '-', w[0]['description'])

# Print temperature.
t = weather_data['main']
temp = t["temp"]-273.15 # Convert Kelvin to 'Celsius
print('Temperature - %.2f\'C' %(temp))
