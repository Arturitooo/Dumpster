import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
#this line handles all the errors that might appear
#response.raise_for_status()

"""#but you can also handle errors on your own
if response.status_code != 200:
    print("Error, something went wrong")"""

#here you make the data into dictionary
data = response.json() 

longitude = data['iss_position']["longitude"]
latitude = data['iss_position']["latitude"]

iss_position = (latitude, longitude)
print(iss_position)

#responses
#1XX hold on..
#2XX here you go
#3XX Go away
#4XX You screwed up
#5XX I screwed up

import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    'lat': MY_LAT,
    'lng':MY_LONG,
    'formatted':0,
}

responsee = requests.get('https://api.sunrise-sunset.org/json', params= parameters)
dataa = responsee.json()
sunrise = dataa['results']['sunrise'].split("T")[1].split(":")[0]
sunset = dataa['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.datetime.now()

print(time_now.hour)

#if dataa['results']['astronomical_twilight_end']

