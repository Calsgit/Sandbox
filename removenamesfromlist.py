names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Remove: ")
while name_to_remove != "":
    if name_to_remove in names:
        names.remove(name_to_remove)
    else:
        print("Name is not in list")
    print(", ".join(names))
    name_to_remove = input("Remove: ")
