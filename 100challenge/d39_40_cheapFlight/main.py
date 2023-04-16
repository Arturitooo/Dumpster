# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import requests
from data_manager import DataManager

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)
