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
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
