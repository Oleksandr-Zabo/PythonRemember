import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RepositoryInterface import RepositoryInterface


class CarRepository(RepositoryInterface):
    def __init__(self):
        self.cars = []

    def create(self, data):
        self.cars.append(data)

    def read_all(self):
        return self.cars

    def update(self, old_data, new_data):
        for i in range(len(self.cars)):
            if self.cars[i] == old_data:
                self.cars[i] = new_data
                return True
        return False

    def delete(self, data):
        for i in range(len(self.cars)):
            if self.cars[i] == data:
                del self.cars[i]
                return True
        return False