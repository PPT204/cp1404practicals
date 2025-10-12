"""
CP1404/CP5632 - Practical
Basic list operations and simple security checker.
"""

def main():
    """Run the main program: number operations and security check."""
    numbers = get_numbers(5)



def get_numbers(count):
    """Prompt the user to enter 'count' numbers and return them as a list of floats."""
    numbers = []
    for i in range(count):
        number = float(input(f"Number: "))
        numbers.append(number)
    return numbers



main()