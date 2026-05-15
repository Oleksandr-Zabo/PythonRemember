# Реалізуйте клас «Книга».
# Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.

class BookEntity:
    def __init__(self, title, year_of_publication, publisher, genre, author, price):
        self.title = title
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title}, Year: {self.year_of_publication}, Publisher: {self.publisher}, Genre: {self.genre}, Author: {self.author}, Price: ${self.price}"