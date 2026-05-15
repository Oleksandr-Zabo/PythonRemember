import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .StadiumEntity import StadiumEntity
from CommandInterface import CommandInterface


class AddStadiumCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        name = input("Enter stadium name: ")
        opening_date = input("Enter opening date (DD.MM.YYYY): ")
        country = input("Enter country: ")
        city = input("Enter city: ")
        capacity = int(input("Enter capacity (people): "))

        stadium = StadiumEntity(name, opening_date, country, city, capacity)
        self.repo.create(stadium)
        print(f"✓ Stadium '{name}' added successfully!")
