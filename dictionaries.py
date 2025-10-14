names = ['Derek', 'Xavier', 'Bob', 'Chantanelle']


def convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(list):
    dictionary = {}
    for name in names:
        dictionary.setdefault(name, len(name))
    return dictionary


name_to_length = convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(names)

print(name_to_length)
