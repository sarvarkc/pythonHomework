a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = input()

if b in a:
    a.update({b: 'new value'})
else:
    print("Key not found")

print(a)