a = [1,2,3,-4,5,6,7,-8,9,-10,11,12,13,-14,15,16]
b = 5
c = []

for x in range(0, len(a), b):
    c.append(a[x:x + b])

print(c)