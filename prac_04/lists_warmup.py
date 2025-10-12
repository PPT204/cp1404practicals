"""
CP1404/CP5632 - Practical
Working with lists
"""
# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]       > 3
# numbers[-1]      > 2
# numbers[3]       > 1
# numbers[:-1]     > [3, 1, 4, 1, 5, 9]
# numbers[3:4]     > [1]
# 5 in numbers     > True
# 7 in numbers     > False
# "3" in numbers   > False
# numbers + [6, 5, 3] > [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

def modify_first_and_last(nums):
    """Change the first element to 'ten' and the last element to 1."""
    nums[0] = "ten"
    nums[-1] = 1


def print_all_except_first_two(nums):
    """Print all elements except the first two using slicing."""
    print(nums[2:])








modify_first_and_last(numbers)
print_all_except_first_two(numbers)