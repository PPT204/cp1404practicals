"""
Ask the user for a password of minimum length and print a line of asterisks matching its length.
"""

MIN_LENGTH = 8

password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Enter a password: ")

print("*" * len(password))
