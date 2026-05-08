import  hashlib
import zlib
HELLO = "Hello World"
print(hashlib.md5(HELLO.encode()).hexdigest())

print(hashlib.sha1(HELLO.encode()).hexdigest())

print(hashlib.sha256(HELLO.encode()).hexdigest())

print(hashlib.sha3_256(HELLO.encode()).hexdigest())

print(hashlib.blake2b(HELLO.encode()).hexdigest())


print()
print(zlib.crc32(HELLO.encode()))

users = {
    "keep1@ghg.dot": {
        "password": hashlib.md5("Qwerty".encode()).hexdigest(),
        "name":'Keep1',
        'age': 25
    },
    "master1@gnm.com":{
        "password": hashlib.md5("12345".encode()).hexdigest(),
        "name":'Master1',
        'age': 12
    }
}

print("-------\nUsers:\n")
print(users)

for user in users.values():
    print(user)
    if user['age'] > 20:
        print(f"user {user['name']} is adult")

sortByAge = sorted(users.values(), key=lambda x: x['age'])
print(sortByAge)

# using lambda in map, filter and reduce
numbers = [1, 2, 3, 4, 5, 6]

squared = map(lambda x: x**2, numbers)
list_comp = [num * 2 for num in numbers] # Compliant
print(list(squared))

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # prints out 720 which is 1*2*3*4*5*6

nested_numbers = [[6, 5, 4], [3, 2, 1]]
flattened = reduce(lambda x, y: x + y, nested_numbers)
print(flattened)  # prints out [6, 5, 4, 3, 2, 1]