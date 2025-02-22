a = []
b = int(input())
c = int(input())

for x in range(c+1):
    if x>=b:
        a.append(x)
new_a = tuple(a)
print(new_a)
