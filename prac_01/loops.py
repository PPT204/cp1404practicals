"""
CP1404/CP5632 - Practical
Loops demonstration
"""

# Constants
LOWER_LIMIT = 1
UPPER_LIMIT = 20
COUNT_STEP = 10

# Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100")
for i in range(0, 101, COUNT_STEP):
    print(i, end=' ')
print("\n")

# Count down from 20 to 1
print("b. Count down from 20 to 1")
for i in range(UPPER_LIMIT, LOWER_LIMIT - 1, -1):
    print(i, end=' ')
print("\n")

# Print a number of stars on one line
print("c. Print a number of stars")
number_of_stars = int(input("Number of stars: "))
print('*' * number_of_stars)
print()

# Print lines of increasing stars
print("d. Print lines of increasing stars")
number_of_lines = int(input("Number of lines: "))
for i in range(1, number_of_lines + 1):
    print('*' * i)
