import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity_fields import IntAtLeast, NonEmptyText, NumberAtLeast, ValidatedField


class BookEntity:
    title = ValidatedField(NonEmptyText("title"))
    year_of_publication = ValidatedField(IntAtLeast("year_of_publication", 1))
    publisher = ValidatedField(NonEmptyText("publisher"))
    genre = ValidatedField(NonEmptyText("genre"))
    author = ValidatedField(NonEmptyText("author"))
    price = ValidatedField(NumberAtLeast("price", 0.0))

    def __init__(self, title, year_of_publication, publisher, genre, author, price):
        self.title = title
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return (
            f"Book: {self.title}, Year: {self.year_of_publication}, Publisher: {self.publisher}, "
            f"Genre: {self.genre}, Author: {self.author}, Price: ${self.price:.2f}"
        )

    @property
    def short_label(self):
        return f"{self.author} - {self.title}"

    def __repr__(self):
        return (
            f"BookEntity(title={self.title!r}, year_of_publication={self.year_of_publication!r}, "
            f"publisher={self.publisher!r}, genre={self.genre!r}, author={self.author!r}, price={self.price!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, BookEntity):
            return NotImplemented
        return (
            self.title,
            self.year_of_publication,
            self.publisher,
            self.genre,
            self.author,
            self.price,
        ) == (
            other.title,
            other.year_of_publication,
            other.publisher,
            other.genre,
            other.author,
            other.price,
        )

    def __lt__(self, other):
        if not isinstance(other, BookEntity):
            return NotImplemented
        return (self.author.lower(), self.title.lower()) < (other.author.lower(), other.title.lower())
