from stats import word_counting, char_counting, listify
import sys

# CLI argument check, suggesting proper usage if wrong

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# takes a filepath as input and returns the contents of the file as a string

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

# main links the values so first the book turns into a string, then it gets split up and counted

def main():
    textbulk = get_book_text(book_path)
    num_words = word_counting(textbulk)
    num_chars = char_counting(textbulk)
    list_chars = listify(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
