class Person:
    def __init__(self, name, age): #self - this in java, this in c#, self - посилання на поточний об'єкт класу
        self.name = name
        self.age = age
        _protected = 'protected variable' # protected variable can be accessed in the same package or subclass
        __private = 'private variable' # private variable can be accessed only in the same class (Pythonic way)

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self): # __str__ - C# toString() - це спеціальний метод, який визначає, як об'єкт буде представлений у вигляді рядка (string).
        return f"Person(name='{self.name}', age={self.age})"