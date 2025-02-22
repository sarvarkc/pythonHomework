a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = input()
if b in a:
    a.pop(b)
else:
    print("Key not found")
print(a)