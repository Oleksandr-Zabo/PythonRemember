import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RepositoryInterface import RepositoryInterface

class StadiumRepository(RepositoryInterface):
    def __init__(self):
        self.stadiums = []

    def create(self, data):
        self.stadiums.append(data)

    def read_all(self):
        return self.stadiums

    def update(self, old_data, new_data):
        for i in range(len(self.stadiums)):
            if self.stadiums[i] == old_data:
                self.stadiums[i] = new_data
                return True
        return False

    def delete(self, data):
        for i in range(len(self.stadiums)):
            if self.stadiums[i] == data:
                del self.stadiums[i]
                return True
        return False