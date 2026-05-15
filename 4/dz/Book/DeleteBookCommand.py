import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class DeleteBookCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        books = self.repo.read_all()
        if not books:
            print("No books available to delete.")
            return

        print('\nBooks available:')
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")

        try:
            index = int(input("Enter book number to delete: ")) - 1
            if 0 <= index < len(books):
                book = books[index]
                self.repo.delete(book)
                print(f"✓ Book '{book.title}' deleted successfully!")
            else:
                print("❌ Invalid selection.")
        except ValueError:
            print("❌ Invalid input.")
