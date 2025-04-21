from stats import get_num_words, get_num_char

def main():

    filepath = "books/frankenstein.txt"

    print(get_num_words(filepath))

    with open(filepath) as f:
        file_contents = f.read()

    print(get_num_char(file_contents))


main()