"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   > When the user enters a non-integer value (e.g., "abc", "3.5", etc.)
2. When will a ZeroDivisionError occur?
   > When the user enters 0 for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   > Yes, by using a while loop to repeatedly ask for a non-zero denominator.
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # Prevent division by zero
        while denominator == 0:
            print("Denominator cannot be zero!")
            denominator = int(input("Enter the denominator: "))

        fraction = numerator / denominator
        print(fraction)
        valid_input = True

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

print("Finished.")
