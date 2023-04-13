# #32. Longest Valid Parentheses
# Hard

# Companies
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
# parentheses
# substring

# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# # Output: 0

def valid_parentheses(a_str):
    a = '('
    b = ')'
    count = 0
    for i, ele in enumerate(a_str):
        if ele == a and a_str[i+1] == b:
            count += 2
    return count


if __name__ == '__main__':
    print(valid_parentheses(")()())"))