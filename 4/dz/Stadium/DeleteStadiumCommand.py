import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class DeleteStadiumCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        stadiums = self.repo.read_all()
        if not stadiums:
            print("No stadiums available to delete.")
            return

        print('\n🏟️  Stadiums available:')
        for i, stadium in enumerate(stadiums, 1):
            print(f"{i}. {stadium}")

        try:
            index = int(input("Enter stadium number to delete: ")) - 1
            if 0 <= index < len(stadiums):
                stadium = stadiums[index]
                self.repo.delete(stadium)
                print(f"✓ Stadium '{stadium.name}' deleted successfully!")
            else:
                print("❌ Invalid selection.")
        except ValueError:
            print("❌ Invalid input.")

