a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = {
    'surname': 'Doe',
    'phone': '1234567890',
    'place': 'New York'
}
c = a
c.update(b)
print(c)