
class UserGetSet:
    def __init__(self, name, age):
        self._name = name      # goes through setter
        self._age = age

    @property
    def name(self):
        return self._name     # read backing field

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value    # IMPORTANT: assign to _name, not name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value