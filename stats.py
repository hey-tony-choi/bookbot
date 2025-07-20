def word_count(text):
    ls = text.split()
    return len(ls)


def letter_count(string):
    word_dict = {}
    for i in range(len(string)):
        letter = string[i].lower()
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    return word_dict


def separate_each(dic):
    result = []
    for key in dic:
        x = {"char":key, "num": dic[key]}
        result.append(x)
    
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(item):
    return item["num"]
