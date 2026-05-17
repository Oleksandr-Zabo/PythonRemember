class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive non zero number")
        else:
            instance.__dict__[self.name] = value


