a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': '50',
    'address': '123 Main St',
    'phone': '555-12'
}
b = {}
for x in a:
    if len(a[x]) > 5:
        b.update({x: a[x]})
print(b)