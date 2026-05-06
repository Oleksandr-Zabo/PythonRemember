# documentStatus = "In Progress", "Need Review", "Approved"
# print(documentStatus[0])
#
# userTypes = ("admin", "student", "teacher")
# user1, user2, user3 = userTypes
# print(user1)
# print(user2)
# print(user3)
#
# user1 = "SuperAdmin"
# userTypes2  = (user1, user2, user3)
# print(userTypes2)

userTypes3 = ("admin", "student", "teacher")
admin, *users, teacher = userTypes3
print(admin)
print(users)
print(type(users))
print(teacher)

admin, *users = userTypes3
print(type(users))
print(users)

for userType in userTypes3:
    print(userType)
    print(type(userType))


sites = ("Awc", "Wiki")
mobileApp = ("Insta", "Facebook")

allTypes = (sites, mobileApp)
print(allTypes)
print(type(allTypes[0]))

allTypes2 = (mobileApp, sites)
print(allTypes2)
print(type(allTypes2[0]))

concT1T2 = allTypes+allTypes2 # ( ('',''), ('',''), ('',''), ('','') )
print(concT1T2)
print(type(concT1T2[0]))

*sitesL,  = sites
print(sitesL)
print(type(sitesL))
if "Wiki" in sitesL:
    print("Wiki is in the list")

sitesA = {"Google", "X", "Wiki"}
sitesB = {"Micro", "Lambda", "Wiki"}

intersection = sitesA & sitesB
print(intersection)
print(type(intersection))

minOne = sitesA | sitesB
print(minOne)


# 1. Определяем множества
white_wool = {"Шон", "Облачко", "Зевс", "Снежок"}
blue_eyes = {"Шон", "Облачко", "Титан", "Пират"}
has_horns = {"Шон", "Зевс", "Титан", "Блэкки"}

# 2. Практика:
# Кто самый крутой (белый, голубоглазый и с рогами)?
the_best = white_wool & blue_eyes & has_horns
print(f"Самый крутой: {the_best}")  # {'Шон'}

# Кто белый и голубоглазый, но БЕЗ рожек?
cute_ones = (white_wool & blue_eyes) - has_horns
print(f"Милашки: {cute_ones}")      # {'Облачко'}

# Список всех барашков, у которых есть ХОТЯ БЫ ОДИН признак из наших кругов
any_feature = white_wool | blue_eyes | has_horns
print(f"Всего в кругах: {len(any_feature)} барашков")
