from stats import get_num_words, get_num_char, sorted_dict
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath) as f:
        file_contents = f.read()

    character_dict = get_num_char(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_words(filepath))
    print("--------- Character Count -------")


    sorted_dict(character_dict)
    print("============= END ===============")

main()