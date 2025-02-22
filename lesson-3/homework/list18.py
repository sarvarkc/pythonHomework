a = [1,2,3,4,5,6,7,8,9,10]
b = [1,4,8]
c = a.copy()

c.extend(b)

if set(c) == set(a):
    print(True)
else:
    print(False)
