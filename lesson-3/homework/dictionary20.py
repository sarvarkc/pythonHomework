a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': 50
}

new_a = dict(sorted(a.items(), key=lambda x: len(x[0])))

print(new_a)