from stats import word_count
from stats import get_char_count
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_results():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    chars = (get_char_count(get_book_text(sys.argv[1])))
    sorted_chars = sort_dict(chars)
    for entry in sorted_chars:
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")

    print("============= END ===============")
def main():
    try:
        print_results()
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()