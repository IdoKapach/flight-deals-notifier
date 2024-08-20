from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_data import UsersData

# getting the flights' conditions and the users' data
sheety_data = DataManager().get_json()
users_data = UsersData().get()

# searching for each destination in the sheet a flight that it's price is lower than the price that was
# noted in the sheet.
for price in sheety_data['prices']:
    flight_data = FlightData(price['city'], price['iataCode'], price['lowestPrice'])
    flight_search = FlightSearch(flight_data)

    data_dict = flight_search.get_all_data()
    # if a flight was found, it's details are sent to each of the users
    if not data_dict:
        continue
    for user_data in users_data:
        note = NotificationManager(data_dict, user_data)
        note.send_message()