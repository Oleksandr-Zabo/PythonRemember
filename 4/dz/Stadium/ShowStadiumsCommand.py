import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class ShowStadiumsCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        print('\n🏟️  List of Stadiums: ')
        stadiums = self.repo.read_all()
        if not stadiums:
            print("No stadiums available.")
        else:
            for i, stadium in enumerate(stadiums, 1):
                print(f"{i}. {stadium}")

