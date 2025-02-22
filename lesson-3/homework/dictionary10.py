a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = input()

if b in a:
    print(b, a[b])
else:
    print("Key not found")