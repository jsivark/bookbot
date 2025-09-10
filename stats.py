from typing import Dict, List

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def count_num_words(text:str) -> int:
    words = text.split()
    return len(words)

def count_chars(text:str) -> Dict:
    text = text.split()
    vocabulary = {}
    for word in text:
        for c in word.lower():
            vocabulary[c] = vocabulary.get(c,0)+1
    return vocabulary

def sort_on(stats:Dict) -> List:
    sort_out = sorted(((v,k) for k,v in stats.items()), reverse = True)
    return sort_out

        