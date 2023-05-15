# Create a function that takes in two words as input and returns a list of three elements, in the following order:
#
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element should have unique letters, and have each letter be alphabetically sorted.
#
# Examples
# letters("sharp", "soap") ➞ ["aps", "hr", "o"]
#
# letters("board", "bored") ➞ ["bdor", "a", "e"]
#
# letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
# letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# # Even with multiple matching letters (e.g. 3 f's), there should
# # only exist a single "f" in your first element.
#
# letters("match", "ham") ➞ ["ahm", "ct", ""]
# # "ham" does not contain any letters that are not found already
# # in "match".
# Notes
# Both words will be in lower case.
# You do not have to worry about punctuation, all words only have letters from [a-z].
# If an element contains no letters, return an empty string (see last example).

def letters(a_str, b_str):

    c_str = ''
    d_str = ''
    a_list = list(b_str)
    c_list = []
    for i in a_str:
        if i in a_list:
            c_str += i
            for k in a_list:
                if k == i:
                    a_list.remove(k)
        else:
            if i not in c_str:
                d_str += i

    e_str = ''.join(a_list)
    f_str = sort_method(c_str)
    g_str = sort_method(d_str)
    h_str = sort_method(e_str)

    c_list.append(f_str)
    c_list.append(g_str)
    c_list.append(h_str)
    return c_list


def sort_method(a_str):
    a_set = set(a_str)
    a_list = list(a_set)
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    b_str = ''.join(a_list)
    if len(b_str) > 0:
        return b_str
    else:
        return ""


if __name__ == '__main__':
    print(letters("sharp", "soap"))
    print()
    print(letters("board", "bored"))
    print()
    print(letters("happiness", "envelope"))
    print()
    print(letters("kerfuffle", "fluffy"))
    print()
    print(letters("match", "ham"))