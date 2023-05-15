"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
"""


def is_valid(s):
    a = list(s)
    for i in range(len(a)-1):
        if a[i] == "(" and a[i+1] == ")" or a[i] == '[' and a[i+1] == ']' or a[i] == '{' and a[i+1] == '}':
            return True
        else:
            return False


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))

