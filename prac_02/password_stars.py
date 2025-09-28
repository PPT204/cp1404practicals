"""
Ask the user for a password of minimum length and print a line of asterisks matching its length.
"""

MIN_LENGTH = 8


def main():
    """Control the program flow: get a valid password and display asterisks"""
    password = get_password()
    display_asterisks(password)


def get_password():
    """Prompt for a password and enforce the minimum length"""
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def display_asterisks(password):
    """Display a line of asterisks equal in length to the password"""
    print("*" * len(password))


main()
