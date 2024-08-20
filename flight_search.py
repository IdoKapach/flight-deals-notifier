from flight_data import FlightData
from datetime import datetime, timedelta
import requests
from os import environ

FLY_FROM = "LON"
# this class is responsible for tracking attractive flight deals
class FlightSearch:

    # searching for flight that fits flight_data
    def __init__(self, flight_data : FlightData):
        self.flight_data = flight_data
        teq_key = environ["teqKey"]
        self.headers = {
            'apikey': teq_key
        }
        self.url = "https://api.tequila.kiwi.com/v2/search"
        fly_to = self.flight_data.code
        fly_from = FLY_FROM

        now = datetime.now()
        day_next_week = now + timedelta(7)
        day_next_week = day_next_week.strftime("%d/%m/%Y")
        day_next_month = now + timedelta(30)
        day_next_month = day_next_month.strftime("%d/%m/%Y")

        max_price = self.flight_data.price

        self.params = {
            'price_to' : max_price,
            'fly_from' : fly_from,
            'fly_to' : fly_to,
            'date_from' : day_next_week,
            'date_to' : day_next_month
        }

        response = requests.get(self.url, params=self.params, headers=self.headers)
        response.raise_for_status()
        self.search_data = response.json()

    # returning dict that fits to the required format
    def get_all_data(self):
        if len(self.search_data["data"]) > 0:
            key_list = ["cityFrom", "cityTo", "flyFrom", "flyTo", "price"]
            data_dict = {key: value for (key, value) in self.search_data["data"][0].items() if key in key_list}
            data_dict["local_arrival"] = self.search_data["data"][0]["local_arrival"].split("T")[0]
            return data_dict
        return None




