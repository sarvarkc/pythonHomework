a = ["apple", "banana", "cherry"]
b = int(input())
c = []

for x in a:
    for y in range(b):
        c.append(x)

print(c)