"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""

# Constant dictionary of colour names and their hex codes
COLOUR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLUE": "#0000FF",
    "BROWN": "#A52A2A"
}

# Ask user for colour name (case-insensitive)
colour_name = input("Enter colour name: ").strip().upper()

while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().upper()