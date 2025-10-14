names = ['Derek', 'Xavier', 'Bob', 'Chantanelle']


def convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(strings):
    string_to_length = {}
    for string in strings:
        string_to_length[string] = len(string)
    return string_to_length

def convert_to_dictionary2(strings):
    return {string: len(string) for string in strings}


# name_to_length = convert_list_of_strings_to_dictionary_of_strings_and_their_respective_lengths(names)
# print(name_to_length)

print(convert_to_dictionary2(names))