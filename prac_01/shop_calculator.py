"""
CP1404/CP5632 - Practical
Shop Calculator Program
"""

# Constants
DISCOUNT_THRESHOLD = 100       # apply discount if total exceeds this
DISCOUNT_RATE = 0.10           # 10% discount

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0.0
for i in range(number_of_items):
    price = float(input(f"Price of item: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT_RATE)


print(f"Total price for {number_of_items} items is ${total_price:.2f}")
