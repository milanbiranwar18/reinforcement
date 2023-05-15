# A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order. Some examples of
# alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop.
#
# Create a function that takes in a sentence as input and returns True if there is at least one alphabetically sorted
# word inside that has a minimum length of 3.
#
# Examples
# is_alphabetically_sorted("Paula has a French accent.") ➞ True
# # "accent" is alphabetically sorted.
# is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
# # Although "by" is alphabetically sorted, it is only 2 letters long.
# Notes
# Do not count words with 2 or fewer characters.
# Ignore punctuation (periods, commas, etc).


def is_alphabetically_sorted(a_str):
    a_list = a_str.split()
    b_list = []
    for ab in a_list:
        i = list(ab)
        for j in range(len(i) - 1, 0, -1):
            for k in range(j):
                if i[k].isupper() or i[k+1].isupper():
                    i[k] = i[k].lower()
                    i[k+1] = i[k+1].lower()
                if i[k] > i[k + 1]:
                    temp = i[k]
                    i[k] = i[k+1]
                    i[k+1] = temp
        b_str = ''.join(i)
        b_list.append(b_str)

    for i in range(len(a_list)):
        if b_list[i][0] == '.':
            a = a_list[i]
            b = a[:3]
            c = b_list[i]
            d = c[1:4]
            if b == d:
                return True
        elif len(a_list[i]) > 3:
            a = a_list[i]
            b = a[:3]
            c = b_list[i]
            d = c[:3]
            if b == d:
                return True
    else:
        return False


if __name__ == '__main__':
    print(is_alphabetically_sorted("Paula has a French accent."))
    print(is_alphabetically_sorted("She sells sea shells by the sea shore."))

    # print(is_alphabetically("Paula has a French accent."))
    # print(is_alphabetically("She sells sea shells by the sea shore."))
