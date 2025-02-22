a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50,
    'age1': 50,
    'age2': 50
}
b = []

for x in a:
    b.append(a[x])

print(len(set(b)))