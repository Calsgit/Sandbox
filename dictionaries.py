names = ['Derek', 'Xavier', 'Bob', 'Chantanelle']


def convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(list):
    string_to_length = {}
    for string in list:
        string_to_length.setdefault(string, len(string))
    return string_to_length


name_to_length = convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(names)

print(name_to_length)
