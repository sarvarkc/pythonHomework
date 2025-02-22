a = ("apple", "banana", "apple", "cherry", "apple")
b = input()
c = list(a)

c.remove(b)
a = tuple(c)

print(a)