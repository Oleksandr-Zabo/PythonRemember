import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .CarEntity import CarEntity
from CommandInterface import CommandInterface


class AddCarCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        model = input("Enter car model: ")
        year = int(input("Enter year of production: "))
        manufacturer = input("Enter manufacturer: ")
        engine_volume = float(input("Enter engine volume (L): "))
        color = input("Enter color: ")
        price = int(input("Enter price: "))

        car = CarEntity(model, year, manufacturer, engine_volume, color, price)
        self.repo.create(car)
        print(f"✓ Car '{manufacturer} {model}' added successfully!")
