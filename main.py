from stats import count_words, count_chars, print_report
import sys

def get_book_text(filepath):
    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = count_words(content)
    chars_dict = count_chars(content)
    sorted_list = print_report(chars_dict)
    
    # print report with format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()