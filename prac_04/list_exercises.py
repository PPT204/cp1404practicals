"""
CP1404/CP5632 - Practical
Basic list operations and simple security checker.
"""

def main():
    """Run the main program: number operations and security check."""
    numbers = get_numbers(5)
    display_number_info(numbers)
    check_user_access()

def get_numbers(count):
    """Prompt the user to enter 'count' numbers and return them as a list of floats."""
    numbers = []
    for i in range(count):
        number = float(input(f"Number: "))
        numbers.append(number)
    return numbers

def display_number_info(numbers):
    """Display first, last, smallest, largest, and average of the list of numbers."""
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers) / len(numbers)

    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average_number}")

def check_user_access():
    """Check if entered username is in the list of authorised usernames."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()