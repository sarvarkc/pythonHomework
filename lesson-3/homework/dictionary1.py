a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = input("Enter the key: ")
if b in a:
    print(a[b])
else:
    print("Key not found")