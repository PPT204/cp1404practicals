"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Dictionary follows PEP 8 formatting:
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Display the dictionary
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

# Ask for user input and normalize to uppercase
state_code = input("Enter short state: ").upper()

while state_code != "":
    # EAFP: try to access directly, handle error if key doesn't exist
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states nicely aligned
print("\nAll states and names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")
