import smtplib
from os import environ

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self, flight_data : dict, user_data: dict):
        self.flight_data = flight_data
        self.user_data = user_data

    def create_message(self):
        data = self.flight_data
        message = \
            f"Dear {self.user_data['firstName']}, we found for you:\n" \
            f" Only {data['price']}£ to fly from {data['cityFrom']}-{data['flyFrom']} to {data['cityTo']}-{data['flyTo']} on {data['local_arrival']}"
        return message


    def send_message(self):
        message = self.create_message()

        my_email = "idopython10@gmail.com"
        password = environ["idopythonPassword2"]

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=self.user_data["email"], msg=f"Subject:Low price flight alert!\n\n{message}".encode('utf-8'))
        connection.close()


