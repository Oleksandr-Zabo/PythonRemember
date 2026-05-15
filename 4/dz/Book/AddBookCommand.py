import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .BookEntity import BookEntity
from CommandInterface import CommandInterface


class AddBookCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self):
        title = input("Enter book title: ")
        year_of_publication = int(input("Enter year of publication: "))
        publisher = input("Enter publisher: ")
        genre = input("Enter genre: ")
        author = input("Enter author: ")
        price = int(input("Enter price: "))

        book = BookEntity(title, year_of_publication, publisher, genre, author, price)
        self.repo.create(book)
        print(f"✓ Book '{title}' added successfully!")
