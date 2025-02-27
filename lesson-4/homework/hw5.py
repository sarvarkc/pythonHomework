password = input("Enter a password: ")

if len(password) < 8:
    print("Password is too short.")
elif password == password.lower():
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")