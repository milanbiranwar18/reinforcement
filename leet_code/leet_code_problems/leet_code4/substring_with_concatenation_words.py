# #30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all
# concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation
# of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
# The output order does not matter. Returning [9,0] is fine too.
# Example 2:
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
# There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
# We return an empty array.
# Example 3:
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
#

def find_sub_string(s, words):
    a_list = []
    for i, b_str in enumerate(words):
        a_str = '' + b_str
        for j in words:
            if b_str!=j:
                a_str+=j
        c_str = '' + b_str
        for j in words[::-1]:
            if b_str!=j:
                c_str+=j
        a_list.append(a_str)
        a_list.append(c_str)
    a_set = set(a_list)
    print(a_set)
    a = [s.index(sub_str) for sub_str in a_set if sub_str in s]
    return a
    # for sub_str in a_list:
    #     if sub_str in s:
    #         print(s.index(sub_str))


if __name__ == '__main__':
    # print(find_sub_string("barfoothefoobarman", ["foo","bar"]))
    # print(find_sub_string("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    # print(find_sub_string("barfoofoobarthefoobarman", ["bar","foo","the"]))
    print(find_sub_string("wordgoodgoodgoodbestword", ["word","good","best","good"]))