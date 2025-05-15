import sys
from stats import get_num_words, get_num_chars, sort_dict 

def main(path_to_file):
    with open(path_to_file) as f:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        file_contents = f.read()
        get_num_words(file_contents)
        print("----------- Character Count ----------")
        dicty = get_num_chars(file_contents)
        sorted_dict = sort_dict(dicty)
        for item in sorted_dict:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])
