a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}
b = {

}
for x in a:
    b.update({a[x]: x})
print(b)