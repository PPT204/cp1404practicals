"""
CP1404/CP5632 - Practical
"""

name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name + "\n")  # write the name on its own line
out_file.close()

in_file = open("name.txt", "r")
stored_name = in_file.read().strip()
in_file.close()
print(f"Hi {stored_name}!")

with open("numbers.txt", "r") as f:
    first = int(f.readline())
    second = int(f.readline())
print(first + second)

total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line.strip())
print(total)