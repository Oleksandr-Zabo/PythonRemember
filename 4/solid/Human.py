class Human:
    def __init__(self, name, birth_date, phone, city, country, adress):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress

    def __str__(self):
        return f"Human{self.name}, {self.birth_date}, {self.phone}, {self.city}, {self.country}, {self.adress}"




