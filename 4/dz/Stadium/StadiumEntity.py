import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity_fields import IntAtLeast, NonEmptyText, ValidatedField


class StadiumEntity:
    name = ValidatedField(NonEmptyText("name"))
    opening_date = ValidatedField(NonEmptyText("opening_date"))
    country = ValidatedField(NonEmptyText("country"))
    city = ValidatedField(NonEmptyText("city"))
    capacity = ValidatedField(IntAtLeast("capacity", 1))

    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Stadium: {self.name}, Opened on: {self.opening_date} in {self.city}, {self.country}. Capacity: {self.capacity} people."

    @property
    def location(self):
        return f"{self.city}, {self.country}"

    def __repr__(self):
        return (
            f"StadiumEntity(name={self.name!r}, opening_date={self.opening_date!r}, country={self.country!r}, "
            f"city={self.city!r}, capacity={self.capacity!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, StadiumEntity):
            return NotImplemented
        return (self.name, self.city, self.country, self.capacity, self.opening_date) == (
            other.name,
            other.city,
            other.country,
            other.capacity,
            other.opening_date,
        )

    def __lt__(self, other):
        if not isinstance(other, StadiumEntity):
            return NotImplemented
        return self.capacity < other.capacity
