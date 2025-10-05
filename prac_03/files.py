"""
CP1404/CP5632 - Practical
"""

name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name + "\n")  # write the name on its own line
out_file.close()
