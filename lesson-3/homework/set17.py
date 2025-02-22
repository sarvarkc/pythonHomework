a = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
b = []
for x in a:
    if x%2!=0:
        b.append(x)
b = set(b)
print(b)  