from datetime import datetime
import requests
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
USERNAME = os.environ['USERNAME']
NUTRITIONIX_API = os.environ["NUTRITIONIX_API"]
SHEETY_API = os.environ['SHEETY_API']
SHEETY_ADDROW_API = os.environ['SHEETY_ADDROW_API']

SHEETY_ADDROW_API = "https://api.sheety.co/b6d9b81549a734f41b4a4ab2e1f6f667/workoutTracking/workouts"

exercise_input = str(input("Tell me which exercises you did: "))

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30,
}

response_nutri = requests.post(
    url=EXERCISE_API, json=exercise_params, headers=headers)

print(response_nutri)
print(response_nutri.text)

### step 4###

today = datetime.now()
DATE_TODAY = today.strftime(f"%d/%m/%Y")
NOW_TIME = today.strftime("%X")

for exercise in response_nutri.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE_TODAY,
            "time": NOW_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ADDROW_API, json=sheet_inputs)

    print(sheet_response.text)


"""response2 = requests.get(
    url='https://api.sheety.co/b6d9b81549a734f41b4a4ab2e1f6f667/workoutTracking/workouts')
print(response2.json())"""
