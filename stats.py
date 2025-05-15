def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_num_chars(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 0
        char_dict[lower_char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(some_dict):
    dict_list = []
    for key, value in some_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
