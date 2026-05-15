# Реалізуйте клас «Стадіон».
# Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.

class StadiumEntity:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Stadium: {self.name}, Opened on: {self.opening_date} in {self.city}, {self.country}. Capacity: {self.capacity} people."