"""
CP1404/CP5632 - Practical
Program to get a valid score, print its result, and show stars equal to the score.
"""

def main():
    """
    Display a menu to get a valid score, show result, or display stars.
    """
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        choice = display_menu()
    print("Farewell! Thank you for using the program.")

def display_menu():


def get_valid_score():


def evaluate_score(score):


def show_stars(score):




main()