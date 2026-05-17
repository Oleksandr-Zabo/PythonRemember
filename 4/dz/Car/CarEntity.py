import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity_fields import IntAtLeast, NonEmptyText, NumberAtLeast, ValidatedField


class CarEntity:
    model = ValidatedField(NonEmptyText("model"))
    year = ValidatedField(IntAtLeast("year", 1886))
    manufacturer = ValidatedField(NonEmptyText("manufacturer"))
    engine_volume = ValidatedField(NumberAtLeast("engine_volume", 0.1))
    color = ValidatedField(NonEmptyText("color"))
    price = ValidatedField(NumberAtLeast("price", 0.0))

    def __init__(self, model: str, year: int, manufacturer: str, engine_volume: float, color: str, price: int):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}) - {self.color}, {self.engine_volume}L, ${self.price:.2f}"

    @property
    def full_name(self):
        return f"{self.manufacturer} {self.model}"

    def __repr__(self):
        return (
            f"CarEntity(model={self.model!r}, year={self.year!r}, manufacturer={self.manufacturer!r}, "
            f"engine_volume={self.engine_volume!r}, color={self.color!r}, price={self.price!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, CarEntity):
            return NotImplemented
        return (
            self.model,
            self.year,
            self.manufacturer,
            self.engine_volume,
            self.color,
            self.price,
        ) == (
            other.model,
            other.year,
            other.manufacturer,
            other.engine_volume,
            other.color,
            other.price,
        )

    def __lt__(self, other):
        if not isinstance(other, CarEntity):
            return NotImplemented
        return (self.year, self.price) < (other.year, other.price)
