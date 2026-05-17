from CallCounter import CallCounter
from BackpackCaller import BackpackCaller

counter = CallCounter()

counter.doClick()
counter.doClick()

counter()
counter()

print( counter.getCount() )

bpFirst = BackpackCaller(20, 20)
print('First:', bpFirst())

print("Fire: ", bpFirst('fire', 5))


