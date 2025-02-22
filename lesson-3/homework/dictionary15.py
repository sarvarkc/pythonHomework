a = ["name", "email", "age"]
b = ["John", "john@gmail.com", 50]
c = {}

for x in range(len(a)):
    c.update({a[x]: b[x]})

print(c)