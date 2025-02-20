a = input()
b = set("aeiou")

new_a = ""

for x in a:
    if x in b:
        new_a += "*"
    else:
        new_a += x

print(new_a)