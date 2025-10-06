names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Remove: ").title()
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Name is not in list")
    print(", ".join(names))
    name_to_remove = input("Remove: ").title()
