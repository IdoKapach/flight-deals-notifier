import requests

# this class is responsible for talking to the google sheet and getting from it the flights' conditions data.
class DataManager:

    def __init__(self):
        sheety_get = requests.get('https://api.sheety.co/194a903f2d68efdf228c542aab1e2357/singleFlight/prices')
        sheety_get.raise_for_status()
        self.sheety_data = sheety_get.json()

    def get_json(self):
        return self.sheety_data