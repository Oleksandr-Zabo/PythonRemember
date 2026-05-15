import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class DeleteCarCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        cars = self.repo.read_all()
        if not cars:
            print("No cars available to delete.")
            return

        print('\nCars available:')
        for i, car in enumerate(cars, 1):
            print(f"{i}. {car}")

        try:
            index = int(input("Enter car number to delete: ")) - 1
            if 0 <= index < len(cars):
                car = cars[index]
                self.repo.delete(car)
                print(f"Car '{car.manufacturer} {car.model}' deleted successfully!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

