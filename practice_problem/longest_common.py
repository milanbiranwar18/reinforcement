# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
def longest_common(a_list):
    if len(a_list) == 1:
        return a_list[0]
    b_list = []
    for i in range(len(a_list)-1):
        a_str = ''
        if len(a_str) == 0:
            for j in a_list[i]:
                if j in a_list[i+1]:
                    a_str += j
        b_list.append(a_str)
    return longest_common(b_list)


if __name__ == '__main__':
    # print(longest_common(["flower","flow","flight"]))
    # print(longest_common(["dog","racecar","car"]))
    print(longest_common(["cir", "car"]))
