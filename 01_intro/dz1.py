tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 9, 8, 2, 7)
tuple3 = (1, 2, 4, 0, 6)

#1
print("#1 (intersection)")
set_1 = set(tuple1) & set(tuple2) & set(tuple3)
print(set_1)

#2
set_2_for1 = set(tuple1) - set(tuple2) - set(tuple3)
print("#2 (difference) for 1")
print(set_2_for1)
set_2_for2 = set(tuple2) - set(tuple1) - set(tuple3)
print("#2 (difference) for 2")
print(set_2_for2)
print("#2 (difference) for 3")
set_2_for3 = set(tuple3) - set(tuple1) - set(tuple2)
print(set_2_for3)

#3
print("#3 (same position in all tuples)")
set_3 = [a for a, b, c in zip(tuple1, tuple2, tuple3) if a == b == c]
print(set_3)