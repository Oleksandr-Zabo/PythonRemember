import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class ShowCarsCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        print('\nList of Cars: ')
        cars = self.repo.read_all()
        if not cars:
            print("No cars available.")
        else:
            for i, car in enumerate(cars, 1):
                print(f"{i}. {car}")

