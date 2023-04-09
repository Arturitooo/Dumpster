import requests
import json 

OWM_Endpoint = "https://api.open-meteo.com/v1/forecast"
api_key = "6d173edad91f52497c3e958157b8a2b4"
weather_params = {
    "latitude" : 54.49,
    "longitude" : 18.22,
    "temperature": "2m",
}

response = requests.get(OWM_Endpoint, params = weather_params)

print(response.status_code) #shows you what's the code of the response, for some rasons i receive 401 which means something is wrong with my authentication, successful request should provide 200 response code
print(response.json())

print("I wasnt able to finish the project since the API used in the course is not available anymore, I couldnt find similar one")