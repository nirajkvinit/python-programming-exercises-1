import random

x = 0
list1 = []
list2 = []

while x < 10:
    list1.append(random.randint(0,50))
    list2.append(random.randint(0,50))
    x += 1

print([i for i in set(list1).intersection(list2)])
