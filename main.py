from stats import count_num_words,get_book_text,count_chars, sort_on
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_num_words(text)
    stats = count_chars(text)
    sort_out = sort_on(stats)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sort_out:
        if i[1].isalpha():
            print(f"{i[1]}: {i[0]}")
    print("============= END ===============")
 
    

if __name__ == "__main__":
    main()