import requests

SHEETY_API = "https://api.sheety.co/b6d9b81549a734f41b4a4ab2e1f6f667/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API)
        self.destination_data = response.json()['prices']
        return self.destination_data

# 6. In the DataManager Class make a PUT request and use the row id
# from sheet_data to update the Google Sheet with the IATA codes. (Do this using code).
# HINT: Remember to check the checkbox to allow PUT requests in Sheety.

    def update_destination_codes(self):
        for city in self.destination_data:
            new_item = {
                'price': {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API}/{city['id']}",
                json=new_item
            )
            print(response.text)
