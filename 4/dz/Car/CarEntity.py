# Реалізуйте клас «Автомобіль».
# Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.

class CarEntity:
    def __init__(self, model: str, year: int, manufacturer: str, engine_volume: float, color: str, price: int):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}) - {self.color}, {self.engine_volume}L, ${self.price}"