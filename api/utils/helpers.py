import re


def cpf_validator(cpf):

    # Has the correct mask?
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return False

    # Grab only numbers
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Does it have 11 digits?
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validate first digit after -
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9],
                                              range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validate second digit after -
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10],
                                              range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
