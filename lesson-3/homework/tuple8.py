a = ("apple", "banana", "apple", "cherry", "ananas")
b = []
b.extend([a[0],a[1],a[2]])
c = tuple(b)

print(c)