class NonEmptyText:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{self.field_name} must be a non-empty string")
        return value.strip()


class IntAtLeast:
    def __init__(self, field_name, minimum=0):
        self.field_name = field_name
        self.minimum = minimum

    def __call__(self, value):
        if not isinstance(value, int) or value < self.minimum:
            raise ValueError(f"{self.field_name} must be an integer >= {self.minimum}")
        return value


class NumberAtLeast:
    def __init__(self, field_name, minimum=0.0):
        self.field_name = field_name
        self.minimum = minimum

    def __call__(self, value):
        if not isinstance(value, (int, float)) or value < self.minimum:
            raise ValueError(f"{self.field_name} must be a number >= {self.minimum}")
        return float(value)


class ValidatedField:
    def __init__(self, validator):
        self.validator = validator
        self.storage_name = None

    def __set_name__(self, owner, name):
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, self.validator(value))

