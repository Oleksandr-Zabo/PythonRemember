"""
🔧 PYTHON MAGIC METHODS (DUNDER METHODS)
Всі спеціальні методи класу __method__()
"""

# ═══════════════════════════════════════════════════════════════════════════
# 1️⃣ INITIALIZATION & REPRESENTATION
# ═══════════════════════════════════════════════════════════════════════════

class Person:
    def __init__(self, name, age):
        """Конструктор - викликається при створенні об'єкта"""
        self.name = name
        self.age = age

    def __str__(self):
        """Повертає читаємий рядок для print()"""
        return f"Person: {self.name}, {self.age} років"

    def __repr__(self):
        """Повертає точний код для відновлення об'єкта"""
        return f"Person(name='{self.name}', age={self.age})"

    def __del__(self):
        """Деструктор - викликається при видаленні об'єкта"""
        print(f"Об'єкт {self.name} видалено")


# Приклад 1: __init__, __str__, __repr__
print("=" * 50)
print("1. INITIALIZATION & REPRESENTATION")
print("=" * 50)

p = Person("Іван", 25)
print(str(p))      # Виводить: Person: Іван, 25 років
print(repr(p))     # Виводить: Person(name='Іван', age=25)


# ═══════════════════════════════════════════════════════════════════════════
# 2️⃣ COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        """== (рівність)"""
        if isinstance(other, Book):
            return self.title == other.title and self.price == other.price
        return False

    def __ne__(self, other):
        """!= (нерівність)"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """< (менше)"""
        return self.price < other.price

    def __le__(self, other):
        """<= (менше або рівно)"""
        return self.price <= other.price

    def __gt__(self, other):
        """> (більше)"""
        return self.price > other.price

    def __ge__(self, other):
        """>= (більше або рівно)"""
        return self.price >= other.price

    def __str__(self):
        return f"{self.title}: ${self.price}"


# Приклад 2: Порівняння об'єктів
print("\n" + "=" * 50)
print("2. COMPARISON OPERATORS")
print("=" * 50)

book1 = Book("Python", 29.99)
book2 = Book("Python", 29.99)
book3 = Book("Java", 39.99)

print(f"book1 == book2: {book1 == book2}")  # True
print(f"book1 != book3: {book1 != book3}")  # True
print(f"book1 < book3: {book1 < book3}")    # True
print(f"book3 > book1: {book3 > book1}")    # True


# ═══════════════════════════════════════════════════════════════════════════
# 3️⃣ ARITHMETIC OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+ (додавання)"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- (віднімання)"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """* (множення на число)"""
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """/ (ділення на число)"""
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        """// (цілочисельне ділення)"""
        return Vector(self.x // scalar, self.y // scalar)

    def __mod__(self, scalar):
        """% (остача від ділення)"""
        return Vector(self.x % scalar, self.y % scalar)

    def __pow__(self, power):
        """** (степінь)"""
        return Vector(self.x ** power, self.y ** power)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Приклад 3: Арифметичні операції
print("\n" + "=" * 50)
print("3. ARITHMETIC OPERATORS")
print("=" * 50)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"{v1} + {v2} = {v1 + v2}")      # Vector(4, 6)
print(f"{v1} - {v2} = {v1 - v2}")      # Vector(2, 2)
print(f"{v1} * 2 = {v1 * 2}")          # Vector(6, 8)
print(f"{v1} / 2 = {v1 / 2}")          # Vector(1.5, 2.0)
print(f"{v1} // 2 = {v1 // 2}")        # Vector(1, 2)


# ═══════════════════════════════════════════════════════════════════════════
# 4️⃣ CONTAINER/INDEXING METHODS
# ═══════════════════════════════════════════════════════════════════════════

class CustomList:
    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        """len() - повертає кількість елементів"""
        return len(self.data)

    def __getitem__(self, index):
        """[] (доступ до елемента)"""
        return self.data[index]

    def __setitem__(self, index, value):
        """[]= (встановлення значення)"""
        self.data[index] = value

    def __delitem__(self, index):
        """del [] (видалення елемента)"""
        del self.data[index]

    def __contains__(self, item):
        """in (перевірка на присутність)"""
        return item in self.data

    def __iter__(self):
        """for loop - ітератор"""
        return iter(self.data)

    def __reversed__(self):
        """reversed() - зворотний порядок"""
        return reversed(self.data)

    def __str__(self):
        return f"CustomList{self.data}"


# Приклад 4: Контейнерні методи
print("\n" + "=" * 50)
print("4. CONTAINER/INDEXING METHODS")
print("=" * 50)

cl = CustomList([1, 2, 3, 4, 5])

print(f"len(cl): {len(cl)}")              # 5
print(f"cl[0]: {cl[0]}")                  # 1
print(f"3 in cl: {3 in cl}")              # True
print(f"Ітерація: {[x for x in cl]}")     # [1, 2, 3, 4, 5]
print(f"Зворотно: {list(reversed(cl))}")  # [5, 4, 3, 2, 1]

cl[0] = 10
print(f"После: {cl}")                      # CustomList[10, 2, 3, 4, 5]


# ═══════════════════════════════════════════════════════════════════════════
# 5️⃣ CALLABLE OBJECTS
# ═══════════════════════════════════════════════════════════════════════════

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Дозволяє використовувати об'єкт як функцію"""
        return x * self.factor


# Приклад 5: Callable об'єкти
print("\n" + "=" * 50)
print("5. CALLABLE OBJECTS (__call__)")
print("=" * 50)

triple = Multiplier(3)
print(f"triple(5) = {triple(5)}")         # 15
print(f"triple(10) = {triple(10)}")       # 30


# ═══════════════════════════════════════════════════════════════════════════
# 6️⃣ ATTRIBUTE ACCESS
# ═══════════════════════════════════════════════════════════════════════════

class DynamicAttributes:
    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
        """Викликається коли атрибут не знайдено"""
        return self._data.get(name, f"Атрибут '{name}' не знайдено")

    def __setattr__(self, name, value):
        """Викликається при встановленні атрибута"""
        if name == "_data":
            super().__setattr__(name, value)
        else:
            print(f"Встановлюю {name} = {value}")
            self._data[name] = value

    def __delattr__(self, name):
        """Викликається при видаленні атрибута"""
        if name in self._data:
            del self._data[name]
            print(f"Видалено {name}")

    def __getattribute__(self, name):
        """Викликається при КОЖНОМУ доступі до атрибута"""
        if name.startswith("_"):
            return super().__getattribute__(name)
        print(f"Доступ до {name}")
        return super().__getattribute__(name)


# Приклад 6: Доступ до атрибутів
print("\n" + "=" * 50)
print("6. ATTRIBUTE ACCESS")
print("=" * 50)

da = DynamicAttributes()
da.name = "John"
da.age = 30
print(f"name: {da.name}")
print(f"missing: {da.missing}")


# ═══════════════════════════════════════════════════════════════════════════
# 7️⃣ CONTEXT MANAGERS
# ═══════════════════════════════════════════════════════════════════════════

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Викликається при входженні в блок with"""
        print(f"Відкриваю файл {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Викликається при виходженні з блоку with"""
        print(f"Закриваю файл {self.filename}")
        if self.file:
            self.file.close()
        return False  # Не придушувати винятки


# Приклад 7: Context Managers
print("\n" + "=" * 50)
print("7. CONTEXT MANAGERS (with statement)")
print("=" * 50)

# with FileManager("test.txt", "w") as f:
#     f.write("Hello, World!")
print("(Приклад виключено - потребує файлової системи)")


# ═══════════════════════════════════════════════════════════════════════════
# 8️⃣ HASH & EQUALITY
# ═══════════════════════════════════════════════════════════════════════════

class UniqPerson:
    def __init__(self, name, passport_id):
        self.name = name
        self.passport_id = passport_id

    def __hash__(self):
        """Дозволяє використовувати об'єкт як ключ словника"""
        return hash(self.passport_id)

    def __eq__(self, other):
        """Потрібна для коректної роботи в наборах"""
        if isinstance(other, UniqPerson):
            return self.passport_id == other.passport_id
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.passport_id})"


# Приклад 8: Хешування
print("\n" + "=" * 50)
print("8. HASH & EQUALITY")
print("=" * 50)

person1 = UniqPerson("Іван", "12345")
person2 = UniqPerson("Петро", "67890")

people_dict = {person1: "інженер", person2: "вчитель"}
print(f"Словник: {people_dict}")

people_set = {person1, person2}
print(f"Набір: {people_set}")


# ═══════════════════════════════════════════════════════════════════════════
# 9️⃣ TYPE CONVERSION
# ═══════════════════════════════════════════════════════════════════════════

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __int__(self):
        """int() - конвертація до цілого числа"""
        return int(self.celsius)

    def __float__(self):
        """float() - конвертація до дійсного числа"""
        return float(self.celsius)

    def __str__(self):
        return f"{self.celsius}°C"

    def __bool__(self):
        """bool() - дорівнює True якщо температура > 0"""
        return self.celsius > 0


# Приклад 9: Конвертація типів
print("\n" + "=" * 50)
print("9. TYPE CONVERSION")
print("=" * 50)

temp = Temperature(25.5)
print(f"Рядок: {str(temp)}")              # 25.5°C
print(f"int: {int(temp)}")                # 25
print(f"float: {float(temp)}")            # 25.5
print(f"bool: {bool(temp)}")              # True


# ═══════════════════════════════════════════════════════════════════════════
# 🔟 DESCRIPTOR PROTOCOL
# ═══════════════════════════════════════════════════════════════════════════

class ValidatedAttribute:
    def __init__(self, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.data = {}

    def __get__(self, obj, objtype=None):
        """Викликається при читанні атрибута"""
        if obj is None:
            return self
        return self.data.get(id(obj), None)

    def __set__(self, obj, value):
        """Викликається при встановленні атрибута"""
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Значення мусить бути від {self.min_val} до {self.max_val}")
        self.data[id(obj)] = value

    def __delete__(self, obj):
        """Викликається при видаленні атрибута"""
        del self.data[id(obj)]


class Student:
    grade = ValidatedAttribute(0, 100)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


# Приклад 10: Descriptors
print("\n" + "=" * 50)
print("10. DESCRIPTOR PROTOCOL")
print("=" * 50)

student = Student("Марія", 85)
print(f"student.grade: {student.grade}")  # 85

try:
    student.grade = 150
except ValueError as e:
    print(f"Помилка: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# 1️⃣1️⃣ SPECIAL NUMERIC METHODS
# ═══════════════════════════════════════════════════════════════════════════

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __pos__(self):
        """Унарний + (позитивне значення)"""
        return Money(self.amount)

    def __neg__(self):
        """Унарний - (протилежне значення)"""
        return Money(-self.amount)

    def __abs__(self):
        """abs() - абсолютне значення"""
        return Money(abs(self.amount))

    def __invert__(self):
        """~ (інверсія)"""
        return Money(-self.amount - 1)

    def __round__(self, ndigits=0):
        """round() - округлення"""
        return Money(round(self.amount, ndigits))

    def __str__(self):
        return f"${self.amount:.2f}"


# Приклад 11: Спеціальні числові методи
print("\n" + "=" * 50)
print("11. SPECIAL NUMERIC METHODS")
print("=" * 50)

money = Money(15.75)
print(f"Оригінал: {money}")               # $15.75
print(f"+money: {+money}")                # $15.75
print(f"-money: {-money}")                # $-15.75
print(f"abs(-money): {abs(-money)}")      # $15.75
print(f"round(money, 1): {round(money, 1)}")  # $15.8


# ═══════════════════════════════════════════════════════════════════════════
# 1️⃣2️⃣ BITWISE OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

class Bits:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        """& (логічне AND)"""
        return Bits(self.value & other.value)

    def __or__(self, other):
        """| (логічне OR)"""
        return Bits(self.value | other.value)

    def __xor__(self, other):
        """^ (логічне XOR)"""
        return Bits(self.value ^ other.value)

    def __lshift__(self, n):
        """<< (зсув вліво)"""
        return Bits(self.value << n)

    def __rshift__(self, n):
        """>> (зсув вправо)"""
        return Bits(self.value >> n)

    def __str__(self):
        return f"Bits({bin(self.value)})"


# Приклад 12: Побітові операції
print("\n" + "=" * 50)
print("12. BITWISE OPERATORS")
print("=" * 50)

b1 = Bits(12)  # 1100
b2 = Bits(10)  # 1010

print(f"{b1} & {b2} = {b1 & b2}")        # Bits(0b1000)
print(f"{b1} | {b2} = {b1 | b2}")        # Bits(0b1110)
print(f"{b1} ^ {b2} = {b1 ^ b2}")        # Bits(0b0110)
print(f"{b1} << 1 = {b1 << 1}")          # Bits(0b11000)
print(f"{b1} >> 1 = {b1 >> 1}")          # Bits(0b110)


# ═══════════════════════════════════════════════════════════════════════════
# 1️⃣3️⃣ CLASS METHODS & METACLASS MAGIC
# ═══════════════════════════════════════════════════════════════════════════

class Animal:
    species = "Невідомо"

    def __init_subclass__(cls, **kwargs):
        """Викликається коли створюється підклас"""
        super().__init_subclass__(**kwargs)
        print(f"Створено підклас {cls.__name__}")

    def __class_getitem__(cls, key):
        """Дозволяє класу підтримувати індексацію"""
        return f"{cls.__name__}[{key}]"


class Dog(Animal):
    """Це автоматично викличе __init_subclass__"""
    pass


# Приклад 13: Підклас і індексація класу
print("\n" + "=" * 50)
print("13. SUBCLASS & CLASS ITEM ACCESS")
print("=" * 50)

print(f"Animal[int]: {Animal[int]}")


# ═══════════════════════════════════════════════════════════════════════════
# ТАБЛИЦЯ ВСІХ МАГІЧНИХ МЕТОДІВ
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("📊 ТАБЛИЦЯ ВСІХ МАГІЧНИХ МЕТОДІВ PYTHON")
print("=" * 70)

magic_methods_table = """
┌─ INITIALIZATION & CLEANUP ─────────────────────────────────────┐
│ __init__(self, ...)           │ Конструктор
│ __del__(self)                 │ Деструктор
│ __new__(cls, ...)             │ Створення об'єкта
└────────────────────────────────────────────────────────────────┘

┌─ STRING REPRESENTATION ────────────────────────────────────────┐
│ __str__(self)                 │ Читаємий рядок (print)
│ __repr__(self)                │ Точна репрезентація
│ __format__(self, format_spec) │ Форматування (f-string)
│ __bytes__(self)               │ Байтовий рядок
└────────────────────────────────────────────────────────────────┘

┌─ COMPARISON ───────────────────────────────────────────────────┐
│ __eq__(self, other)           │ == (рівність)
│ __ne__(self, other)           │ != (нерівність)
│ __lt__(self, other)           │ < (менше)
│ __le__(self, other)           │ <= (менше або рівно)
│ __gt__(self, other)           │ > (більше)
│ __ge__(self, other)           │ >= (більше або рівно)
└────────────────────────────────────────────────────────────────┘

┌─ ARITHMETIC ───────────────────────────────────────────────────┐
│ __add__(self, other)          │ + (додавання)
│ __sub__(self, other)          │ - (віднімання)
│ __mul__(self, other)          │ * (множення)
│ __truediv__(self, other)      │ / (ділення)
│ __floordiv__(self, other)     │ // (цілочислене ділення)
│ __mod__(self, other)          │ % (остача)
│ __pow__(self, other)          │ ** (степінь)
│ __divmod__(self, other)       │ divmod() - (ділення і остача)
└────────────────────────────────────────────────────────────────┘

┌─ REFLECTED ARITHMETIC ─────────────────────────────────────────┐
│ __radd__, __rsub__, __rmul__  │ Обернені операції (2 + obj)
│ __rtruediv__, __rfloordiv__   │ Обернене ділення
│ __rmod__, __rpow__            │ Обернені степень і остача
└────────────────────────────────────────────────────────────────┘

┌─ AUGMENTED ASSIGNMENT ─────────────────────────────────────────┐
│ __iadd__(self, other)         │ += (додавання з присвоєнням)
│ __isub__, __imul__            │ -= (*=) (аналогічно)
│ __itruediv__, __ifloordiv__   │ /= (//=) (аналогічно)
│ __imod__, __ipow__            │ %= (**=) (аналогічно)
│ __iand__, __ior__, __ixor__   │ &= |= ^= (побітові)
│ __ilshift__, __irshift__      │ <<= >>= (зсуви)
└────────────────────────────────────────────────────────────────┘

┌─ UNARY OPERATORS ──────────────────────────────────────────────┐
│ __pos__(self)                 │ + (унарний плюс)
│ __neg__(self)                 │ - (унарний мінус)
│ __abs__(self)                 │ abs() (абсолютне значення)
│ __invert__(self)              │ ~ (інверсія)
└────────────────────────────────────────────────────────────────┘

┌─ BITWISE OPERATORS ────────────────────────────────────────────┐
│ __and__(self, other)          │ & (логічне AND)
│ __or__(self, other)           │ | (логічне OR)
│ __xor__(self, other)          │ ^ (логічне XOR)
│ __lshift__(self, other)       │ << (зсув вліво)
│ __rshift__(self, other)       │ >> (зсув вправо)
└────────────────────────────────────────────────────────────────┘

┌─ CONTAINER METHODS ────────────────────────────────────────────┐
│ __len__(self)                 │ len() (кількість елементів)
│ __getitem__(self, key)        │ obj[key] (доступ до елемента)
│ __setitem__(self, key, value) │ obj[key] = value (встановлення)
│ __delitem__(self, key)        │ del obj[key] (видалення)
│ __contains__(self, item)      │ item in obj (перевірка)
│ __missing__(self, key)        │ dict.get() без ключа
└────────────────────────────────────────────────────────────────┘

┌─ ITERATION ────────────────────────────────────────────────────┐
│ __iter__(self)                │ iter() (створення ітератора)
│ __next__(self)                │ next() (наступний елемент)
│ __reversed__(self)            │ reversed() (зворотний порядок)
└────────────────────────────────────────────────────────────────┘

┌─ ATTRIBUTE ACCESS ─────────────────────────────────────────────┐
│ __getattr__(self, name)       │ Доступ до неіснуючого атрибута
│ __setattr__(self, name, val)  │ Встановлення атрибута
│ __delattr__(self, name)       │ Видалення атрибута
│ __getattribute__(self, name)  │ ВСІ доступи до атрибутів
│ __dir__(self)                 │ dir() (список атрибутів)
└────────────────────────────────────────────────────────────────┘

┌─ CALLABLE OBJECTS ─────────────────────────────────────────────┐
│ __call__(self, ...)           │ obj() (виклик об'єкта як функції)
└────────────────────────────────────────────────────────────────┘

┌─ CONTEXT MANAGERS ─────────────────────────────────────────────┐
│ __enter__(self)               │ Вхід в блок with
│ __exit__(self, exc, ...)      │ Вихід з блоку with
│ __aenter__(self)              │ Асинхронний enter
│ __aexit__(self, exc, ...)     │ Асинхронний exit
└────────────────────────────────────────────────────────────────┘

┌─ TYPE CONVERSION ──────────────────────────────────────────────┐
│ __int__(self)                 │ int() (конвертація в число)
│ __float__(self)               │ float() (конвертація у дійсне)
│ __complex__(self)             │ complex() (конвертація)
│ __bool__(self)                │ bool() (істинне/хибне)
│ __index__(self)               │ Індексація (для слайсів)
└────────────────────────────────────────────────────────────────┘

┌─ HASHING ──────────────────────────────────────────────────────┐
│ __hash__(self)                │ hash() (хеш об'єкта)
│ __eq__(self, other)           │ Для коректної роботи в set/dict
└────────────────────────────────────────────────────────────────┘

┌─ DESCRIPTOR PROTOCOL ──────────────────────────────────────────┐
│ __get__(self, obj, type)      │ Доступ до дескриптора
│ __set__(self, obj, value)     │ Встановлення через дескриптор
│ __delete__(self, obj)         │ Видалення через дескриптор
│ __set_name__(self, owner, nm) │ Назва атрибута при створенні
└────────────────────────────────────────────────────────────────┘

┌─ CLASS METHODS ────────────────────────────────────────────────┐
│ __init_subclass__(cls, **kw)  │ Коли створюється підклас
│ __class_getitem__(cls, key)   │ Класова індексація (Class[int])
│ __prepare__(mcs, name, bases) │ Підготовка простору імен
│ __mro_entries__(self, bases)  │ Базові класи при успадкуванні
└────────────────────────────────────────────────────────────────┘

┌─ SPECIAL ──────────────────────────────────────────────────────┐
│ __sizeof__(self)              │ sys.getsizeof() (розмір пам'яті)
│ __reduce__(self)              │ pickle (серіалізація)
│ __reduce_ex__(self, protocol) │ pickle з протоколом
└────────────────────────────────────────────────────────────────┘
"""

print(magic_methods_table)

print("\n" + "=" * 70)
print("✅ ВСІ ПРИКЛАДИ ЗАВЕРШЕНІ!")
print("=" * 70)