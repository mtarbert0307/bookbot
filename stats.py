
def word_count(book_string):
    words = book_string.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_char_count(chars):
    char_dict = {}
    for char in chars:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    new_list = []
    for entry in dict:
        char_count = {}
        char_count["name"] = entry
        char_count["num"] = dict[entry]
        new_list.append(char_count)
    new_list.sort(reverse=True, key=sort_on)
    

    return new_list