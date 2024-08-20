class FlightData:
    def __init__(self, city, code, price):
        self.city = city
        self.code = code
        self.price = price

    def print(self):
        print(self.city)
        print(self.code)
        print(self.price)