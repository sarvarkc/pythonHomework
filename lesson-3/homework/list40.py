a = [2,3,1,4,4,5,6,8,7,5,8,9]
b = []

for x in a:
    if x not in b:
        b.append(x) 

print(b)