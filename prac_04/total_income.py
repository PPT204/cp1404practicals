"""
CP1404/CP5632 Practical
Cumulative total income program
"""


def main():
    """Ask the user for incomes and display a cumulative income report."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    print_report(incomes)


def get_incomes(number_of_months):
    """Prompt user to enter incomes for each month and return a list of incomes."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def print_report(incomes):
    """Print a formatted income report showing cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
