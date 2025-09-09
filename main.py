from stats import count_num_words,get_book_text

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_num_words(text)
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()