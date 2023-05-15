# Create a function which takes every letter in every word, and puts it in alphabetical order. Note how the original
# word lengths must stay the same.
#
# Examples
# true_alphabetic("hello world") ➞ "dehll loorw"
#
# true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
#
# true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"
# Notes
# All sentences will be in lowercase.
# No punctuation or numbers will be included in the Tests.

def true_alphabetic(a_str):
    a_list = list(a_str)
    # print(a_list)
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

    b_str = ''
    b_list = a_str.split()
    # print(a_list)
    for i in b_list:
        # print(len(i))
        # b_str += " "
        print(a_list)
        c_str = ''
        for j in a_list:
            print(j)
            if j == '':
                continue
            elif len(i) > len(c_str):
                c_str += j
                a_list.remove(j)
        b_str += c_str + " "
        # print(c_str)
        # print(a_list)
    # return b_str

    # i = 0

    # while len(a_list) > 0:
    #     c_str = ''
    #     for k in a_list:
    #         if len(a_list[i]) > len(c_str):
    #             c_str += k
    #             a_list.remove(k)
    #     b_str += c_str + " "
    #     i += 1
    # print(b_str)


if __name__ == '__main__':
    print(true_alphabetic("hello world"))