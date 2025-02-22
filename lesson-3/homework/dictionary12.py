a = {
    'name': "John",
    'email': 'John',
    'age': 50
}
b = []
for x in a:
    if a[x] == 'John':
        b.append(x)
print(len(b))