from Person import Person

class Student(Person):
    def __init__(self, name: str, age: int, grade: str = "Freshman"):
        super().__init__(name, age)
        self.grade = grade
    def study(self):
        print(f"{self.name} is studying.")

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"

s = Student("Alex", 18)
print(s)