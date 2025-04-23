def words_in_book(words):
    word_list = words.split()
    numWords = len(word_list)
    return f"Found {numWords} total words"

def chars_in_book(words):
    char_count = {}
    for c in words.lower():
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def report(char_dict):
    char_list = []
    for char,count in char_dict.items():
        char_list.append({"char": char,"count": count})
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list