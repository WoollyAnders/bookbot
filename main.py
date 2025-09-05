#main.py for bookbot
import sys

from stats import get_book_text, word_count, letter_count, sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    count = word_count(text)
    chars = letter_count(text)
    sorted_items = sort_chars(chars)
    
    for item in sorted_items:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()