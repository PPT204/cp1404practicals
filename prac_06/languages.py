"""
Languages demo
Estimate: 10 minutes
Actual:
"""

from programming_language import ProgrammingLanguage


def main():
    """Create languages, print one, and list those with dynamic typing."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Quick sanity check
    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)


if __name__ == "__main__":
    main()