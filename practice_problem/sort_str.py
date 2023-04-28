# The function is given two strings t - template, s - to be sorted. Sort the characters in s such that if the character
# is present in t then it is sorted according to the order in t and other characters are sorted alphabetically after the
# ones found in t.
#
# Examples
# custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"
#
# custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"
#
# custom_sort("", "abcdefzyx") ➞ "abcdefxyz"
#
# custom_sort("", "") ➞ ""
# Notes
# The characters in t and s are all lower-case.

def custom_sort(t, s):
    a_str = ''
    a_list = list(s)
    for i in t:
        if i in a_list:
            a_str += i
            a_list.remove(i)
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
    b_str = ''.join(a_list)
    return a_str + b_str


if __name__ == '__main__':
    print(custom_sort("edc", "abcdefzyx"))
    print(custom_sort("fby", "abcdefzyx"))
    print(custom_sort("", "abcdefzyx"))
    print(custom_sort("", ""))
