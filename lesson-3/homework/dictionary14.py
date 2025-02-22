a = {
    'name': "John",
    'email': 'John',
    'age': 50
}
b = 'John'
c = []
for x in a:
    if a[x] == b:
        c.append(x)
print(c)