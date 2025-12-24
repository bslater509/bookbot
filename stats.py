def count_num_words(book_path):
    with open(book_path) as f:
        words =f.read().split()
        total = len(words)
        return total

def count_num_characters(book_path):
    with open(book_path) as f:
        characters_dict = {}
        for letter in f.read():
            characters_dict[letter.lower()] = characters_dict.get(letter.lower(), 0) + 1

    return characters_dict

def sort_char_count_dict(book_path):
    char_dict = count_num_characters(book_path)
    alpha_list = []
    for letter in char_dict:
        if letter.isalpha():
            alpha_list.append({"char": letter, "num": char_dict[letter]})
    alpha_list.sort(key=sort_on, reverse=True)
    return alpha_list


def sort_on(items):
    return items["num"]