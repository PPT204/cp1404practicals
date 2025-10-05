"""
CP1404/CP5632 - Practical
Random number examples
"""

import random

# Smallest = 5, largest = 20
print(random.randint(5, 20))
# Smallest possible: 5, largest possible: 20

# Possible values: 3, 5, 7, 9 (cannot be 4)
print(random.randrange(3, 10, 2))
# Smallest: 3, largest: 9
# Could line 2 have produced a 4? -> No, because step=2 skips even numbers.

# Produces a float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
# Smallest possible: 2.5, largest possible: 5.5

# Random integer between 1 and 100
print(random.randint(1, 100))
