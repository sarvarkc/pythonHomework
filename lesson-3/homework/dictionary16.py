a = {
    'name': "John",
    'email': 'john@gmail.com',
    'age': {'age1':50, 'age2': 60}
}
for x in a:
    if type(a[x]) == dict:
        print("Dictionary contains another dictionary")
        break

