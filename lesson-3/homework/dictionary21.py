a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': '50000000000000000000'
}

new_a = dict(sorted(a.items(), key=lambda x: len(x[1])))

print(new_a)