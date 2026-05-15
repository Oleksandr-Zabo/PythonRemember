import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CommandInterface import CommandInterface


class ShowBooksCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        print('\nList of books: ')
        books = self.repo.read_all()
        if not books:
            print("No books available.")
        else:
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
