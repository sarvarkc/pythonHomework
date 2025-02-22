a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = {
    'surname': "John",
    'emaill': 'john@gmail.com',
    'agee': 50
}
new_a = []
new_b = []

for x in a:
    new_a.append(x)
for x in b:
    new_b.append(x)

if set(new_a).intersection(new_b) == set():
    print("No common keys")
else:
    print("Common keys found")