from Book.BookRepository import BookRepository
from Book.AddBookCommand import AddBookCommand
from Book.ShowBooksCommand import ShowBooksCommand
from Book.DeleteBookCommand import DeleteBookCommand
from Car.CarRepository import CarRepository
from Car.AddCarCommand import AddCarCommand
from Car.ShowCarsCommand import ShowCarsCommand
from Car.DeleteCarCommand import DeleteCarCommand
from Stadium.StadiumRepository import StadiumRepository
from Stadium.AddStadiumCommand import AddStadiumCommand
from Stadium.ShowStadiumsCommand import ShowStadiumsCommand
from Stadium.DeleteStadiumCommand import DeleteStadiumCommand


class ConsoleUI:
    def __init__(self):
        self.book_repo = BookRepository()
        self.car_repo = CarRepository()
        self.stadium_repo = StadiumRepository()

        self.book_commands = {
            '1': AddBookCommand(self.book_repo),
            '2': ShowBooksCommand(self.book_repo),
            '3': DeleteBookCommand(self.book_repo),
        }
        self.car_commands = {
            '1': AddCarCommand(self.car_repo),
            '2': ShowCarsCommand(self.car_repo),
            '3': DeleteCarCommand(self.car_repo),
        }
        self.stadium_commands = {
            '1': AddStadiumCommand(self.stadium_repo),
            '2': ShowStadiumsCommand(self.stadium_repo),
            '3': DeleteStadiumCommand(self.stadium_repo),
        }

    def run(self):
        print("=== Welcome to Database Management ===")
        while True:
            print("\nChoose management type:")
            print("1: Books")
            print("2: Cars")
            print("3: Stadiums")
            print("0: Exit")
            choice = input("Select type: ").strip()

            if choice == '1':
                self._run_menu("Book", self.book_commands)
            elif choice == '2':
                self._run_menu("Car", self.car_commands)
            elif choice == '3':
                self._run_menu("Stadium", self.stadium_commands)
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Unknown management type. Try again.")

    def _run_menu(self, title, commands):
        while True:
            print(f"\n=== {title} management ===")
            print("1: Add")
            print("2: Show")
            print("3: Delete")
            print("0: Back")
            choice = input("Select action: ").strip()

            if choice == '0':
                return

            command = commands.get(choice)
            if command:
                try:
                    command.execute()
                except Exception as exc:
                    print(f"Error: {exc}")
            else:
                print("Unknown command. Try again.")
