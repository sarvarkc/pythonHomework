import random

a = []
b = int(input())

for x in range(b):
    a.append(random.randint(1, 100))

print(a)