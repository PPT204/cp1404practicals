"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 0.0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    rate = 0.15 if sales >= 1000 else 0.10
    print(f"Your bonus is: ${sales * rate:.2f}")

print("Done.")