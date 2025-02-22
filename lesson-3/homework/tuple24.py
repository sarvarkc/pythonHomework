a = ('a', 'b', 'b', 'a')
b = list(a).copy()
b.reverse()
b = tuple(b)

print(bool(a == b))
