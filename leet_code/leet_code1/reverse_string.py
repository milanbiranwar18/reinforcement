#344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
def reverse_string(s):
    return s[::-1]
    # return [s[i] for i in range(len(s)-1, -1, -1)]


if __name__ == '__main__':
    print(reverse_string(["h","e","l","l","o"]))
    print(reverse_string(["H","a","n","n","a","h"]))