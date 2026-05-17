from UserGetSet import UserGetSet

u = UserGetSet('John Doe', 25)
print(u.name, u.age)

u.name = "Jane"
u.age = 30
print(u.name, u.age)