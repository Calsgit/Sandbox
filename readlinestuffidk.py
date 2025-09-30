try:
    count = 1
    name = ""
    age = 0
    infile = open("readlineinfo.txt", 'r')
    for line in infile.readline():
        line.strip()
        if count % 2 == 0:
            try:
                age = int(line)
            except # uhhh yeah
except FileNotFoundError:
    print("File does not exist")