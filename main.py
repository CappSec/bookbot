from stats import words_in_book
from stats import chars_in_book
from stats import report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
   # book = get_book_text("books/frankenstein.txt")
    print("----------- Word Count ----------\n")
    words = words_in_book(book)
    print(f"{words}\n")
    print("--------- Character Count -------")
    chars = chars_in_book(book)
    char_report = report(chars)
    for i in char_report:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']}")

main()

