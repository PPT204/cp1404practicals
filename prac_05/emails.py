"""
Emails
Estimate: 20 minutes
Actual: 17 minutes
"""

def main():
    """Store emails and associated names, then display them."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    # Print all stored emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract a formatted name from the email address."""
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').split()
    return ' '.join(part.title() for part in parts)


main()
