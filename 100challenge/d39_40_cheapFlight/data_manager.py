import requests

SHEETY_GET = "https://api.sheety.co/b6d9b81549a734f41b4a4ab2e1f6f667/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET)
        destination_data = response.json()['prices']
        return destination_data
