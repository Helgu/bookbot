def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")



def get_num_unique_chars(text):
    text = text.lower()
    symbols = set(text)
    symbol_counts = {}

    for symbol in symbols:
        symbol_counts[symbol] = text.count(symbol)
    return symbol_counts

def sort_on(items):
    return items["num"]



def sort_list(dictionary):
    # {"char" : "x", "num" : 32423}
    sorted_dict = []
    
    for char in dictionary.keys():
        if(char.isalpha()):
            item = {}
            item["char"] = char
            item["num"] = dictionary[char]
            sorted_dict.append(item)

    sorted_dict.sort(reverse=True,key=sort_on)
    return sorted_dict