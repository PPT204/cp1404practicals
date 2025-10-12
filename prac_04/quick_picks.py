"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    """Ask for number of quick picks and generate each lottery line."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():




def print_quick_pick(quick_pick):



main()