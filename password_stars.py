password = input("Password: ")
while len(password) < 5:
    print("Password is too small, must be 5 or more characters")
    password = input("Password: ")
print("*" * len(password))
