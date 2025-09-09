from typing import Dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def count_num_words(text:str) -> int:
    words = text.split()
    return len(words)

def count_chars(text:str) -> Dict:
    text = text.split()
    vocabulary = {}
    unique_values = set(text)
    for c in text:
        

        