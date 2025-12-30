import sys
from stats import get_num_words, get_num_unique_chars, sort_list


def get_book_text(path):
    
    with open(path) as f:
        file_contents = f.read()
        
    return file_contents


def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)




        
    path = sys.argv[1]
    get_num_words(get_book_text(path=path))
    unique_count = sort_list(get_num_unique_chars(get_book_text(path=path)))
    for i in unique_count:
        print(f"{i["char"]}: {i["num"]}")

main()