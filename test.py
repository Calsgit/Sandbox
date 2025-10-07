from operator import itemgetter

# numbers = [1, 5, 7, 4]
# string_numbers = [str(number) for number in numbers]
# print("/".join(string_numbers))

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
max_length = max((len(pair[0]) for pair in data))
for pair in sorted(data, key=itemgetter(1), reverse=True):
    name, score = pair
    print(f"{name:<{max_length}} ={score:>4}")

# ITEMGETTER!!!!!!!