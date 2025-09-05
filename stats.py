def get_book_text(path):
    with open(path, "r") as f:
        book_text = f.read()
    return book_text

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    count = word_count(text)
    print(f"{count} words found in the document")

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(words):
    letters = {}
    lowercase = words.lower()
    for ch in lowercase:
        letters[ch] = letters.get(ch, 0) + 1
    return letters

def sort_on(item):
        return item["num"]

def sort_chars(char_counts):
    items = []
    for char, count in char_counts.items():
        items.append({"char": char, "num": count})
    items.sort(key=sort_on, reverse=True)
    return items    
