import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RepositoryInterface import RepositoryInterface

class BookRepository(RepositoryInterface):
    def __init__(self):
        self.books = []

    def create(self, data):
        self.books.append(data)

    def read(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def read_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def read_all(self):
        return self.books

    def update(self, old_data, new_data):
        for i in range(len(self.books)):
            if self.books[i] == old_data:
                self.books[i] = new_data
                return True
        return False

    def delete(self, data):
        for i in range(len(self.books)):
            if self.books[i] == data:
                del self.books[i]
                return True
        return False