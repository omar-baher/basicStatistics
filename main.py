import random


def print_header():
    print()
    print('----------------------------------------------------------------------------------------------------------')
    print('---------------------------- Welcome to my basic statistics application ----------------------------------')
    print('This application will generate random numbers and calculate the following:\n'
          'Total, Average, Max, Min and list of numbers divisible by 5')
    print('----------------------------------------------------------------------------------------------------------')
    print()


def generate_random_numbers():
    number_list = []
    required_numbers = int(input('How many random numbers do you want to generate? '))

    for number in range(0, required_numbers):
        number_list.append(random.randint(0, 100))

    return number_list


def get_numbers_divisible_by_5(number_list: list) -> list:
    numbers_divisible_by_5_list = []

    for number in number_list:
        remainder = number % 5
        if remainder == 0:
            numbers_divisible_by_5_list.append(number)

    return numbers_divisible_by_5_list


def get_total(number_list: list) -> int:
    total_value = 0
    for number in number_list:
        total_value = total_value + number

    return total_value


def get_average(total_value: int, number_list: list) -> float:
    return total_value / len(number_list)


def get_max_number(number_list: list) -> int:
    max_number_value = 0
    for item in number_list:
        if item > max_number_value:
            max_number_value = item
    return max_number_value


def get_min_number(number_list: list) -> int:
    min_number_value = number_list[0]
    for item in number_list:
        if item < min_number_value:
            min_number_value = item
    return min_number_value


print_header()
numbers: list = generate_random_numbers()
numbers_divisible_by_5: list = get_numbers_divisible_by_5(numbers)
total: int = get_total(numbers)
average_number: float = get_average(total, numbers)
max_number: int = get_max_number(numbers)
min_number: int = get_min_number(numbers)


print(f'The random numbers are: \n {numbers} \n')
print(f'The numbers that are divisible by 5 are: \n {numbers_divisible_by_5}\n')
print(f'The sum of all numbers is: {total}')
print(f'The average of all numbers is: {average_number}')
print(f'The max number is {max_number}')
print(f'The min number is {min_number}')

print()
print('Thank you for using my application')
print('Developed by Omar Elkobia')
print('Follow my github account for future versions...')