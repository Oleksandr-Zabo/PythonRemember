#1
print('#1')
def fibonacci_range(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            yield a
        a, b = b, a + b

for num in fibonacci_range(0, 100):
    print(num)


#2
print('\n#2')
def sum_lists(list1, list2):
    # Доповнимо довжини однаковими елементами нульовими
    if len(list1) < len(list2):
        list1.extend([0] * (len(list2)-len(list1)))
    elif len(list1) > len(list2):
        list2.extend([0] * (len(list1)-len(list2)))

    # Використовуємо генератор для повернення суми елементів списку
    return [a + b for a, b in zip(list1, list2)]

print(sum_lists([1, 3, 4, 2],[8, 3, 5, 9])) # Виводить: [9, 6, 9, 11]

#3
print('\n#3')
def calculate(list_to_work, function_to_call):
    return [function_to_call(num) for num in list_to_work]  # Використовуємо функцію для зміни значень елементів списку

# Приклади використання:
squared = calculate([1, 2, 3, 4], lambda x: x ** 2) # [1, 4, 9, 16] - квадрати чисел
cubed = calculate([1, 2, 3, 4], lambda x: x ** 3)   # [1, 8, 27, 64] - кубічники чисел
print(squared, ' and ', cubed)

#4
print('\n#4')
def report_decorator(report_func):   # Декоратор, який оголошує функцію звітності
    def inner(*args, **kwargs):       # Внутрішня функція, в яку передано аргументи для звіту
        print('Зміна стану компанії.')   # Виконання початкового завдання декоратора
        report_func(*args, **kwargs)    # Виклик оригінальної функції звіту з переданими аргументами
        print('Зміна стану компанії завершено.')  # Виконання кінцевого завдання декоратора
    return inner                       # Повернення внутрішньої функції у вигляді декорованої

# Приклад використання:
@report_decorator     # Декорування звітної функції
def financial_report(year):   # Звичайна функція звіту про фінанси за роки
    print(f'Звіт про фінанси {year} року.')

financial_report(2023)  # Виконання звичайної функції звіту


