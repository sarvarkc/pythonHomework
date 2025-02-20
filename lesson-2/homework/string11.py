a = input()
digits = set("0123456789")

if set(a) & digits:
    print(True)
else:
    print(False)