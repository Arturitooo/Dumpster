import requests
from pprint import pprint

fs_API_locations = "https://api.tequila.kiwi.com/locations/query"
fs_API_key = 'F3gHkCDxDuH7zOcVsh2Z2TM25Bllt5vU'
fs_API_header = {
    "apikey": fs_API_key
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        query = {'term': city_name, 'location_types': 'city'}
        request = requests.get(
            url=fs_API_locations, params=query, headers=fs_API_header)
        results = request.json()['locations']
        code = results[0]['code']
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        return code
