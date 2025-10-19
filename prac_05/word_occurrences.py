"""
Word Occurrences
Estimate: 20 minutes
Actual: 28 minutes
"""

def main():
    """Count and display the occurrences of words in a string."""
    text = input("Text: ")
    words = text.split()

    # Count occurrences of each word
    word_to_count = {}
    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Find the maximum word length for formatting
    max_length = max(len(word) for word in word_to_count)

    # Display sorted output, neatly aligned
    for word in sorted(word_to_count):
        print(f"{word:{max_length}} : {word_to_count[word]}")

main()