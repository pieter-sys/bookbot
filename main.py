from stats import word_counting, char_counting

# takes a filepath as input and returns the contents of the file as a string
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

# main links the values so first the book turns into a string, then it gets split up and counted
def main():
    textbulk = get_book_text("./books/frankenstein.txt")
    num_words = word_counting(textbulk)
    num_chars = char_counting(textbulk)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
