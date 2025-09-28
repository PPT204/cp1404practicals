"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Ask the user for a score and print the result, then generate a random score and print its result"""
    score = float(input("Enter score: "))
    print(evaluate_score(score))

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(evaluate_score(random_score))


def evaluate_score(score):
    """Determine the grade string based on the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
