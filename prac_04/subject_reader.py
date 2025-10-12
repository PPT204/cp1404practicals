"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and display subject details."""
    subjects = load_data(FILENAME)
    display_subjects(subjects)

def load_data(filename):
    """
    Read data from file formatted like: subject_code,lecturer_name,number_of_students
    Return the data as a list of lists.
    """
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2])  # convert number of students to int
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display formatted details for each subject."""
    for subject_code, lecturer_name, num_students in subjects:
        print(f"{subject_code} is taught by {lecturer_name} and has {num_students} students")

main()
