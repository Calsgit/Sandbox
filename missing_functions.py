def main():
    numbers = get_numbers()
    print(numbers)
    square_numbers(numbers)
    display_numbers(numbers)


def get_numbers():
    string_of_numbers = input("Enter numbers separated by commas: ")
    string_of_numbers = string_of_numbers.replace(' ', '')
    list_of_number_strings = string_of_numbers.split(',')
    numbers = [float(number) for number in list_of_number_strings]
    return numbers


def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2


def display_numbers(numbers):
    print("..".join([str(number) for number in numbers]))


main()
