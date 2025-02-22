a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = input("Enter the key: ")
a.setdefault(b, 'No value')
print(a[b])