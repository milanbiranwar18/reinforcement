# #Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    cur_word = strs[0]
    for i in range(1, len(strs)):
        a_str = ""
        for j in range(len(strs[i])):
            if j < len(cur_word) and cur_word[j] == strs[i][j]:
                a_str += cur_word[j]
            else:
                break
        if len(cur_word) == 0:
            break
        cur_word = a_str
    if len(strs) == 0:
        return ""
    return cur_word


if __name__ == '__main__':
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["dog","racecar","car"]))
