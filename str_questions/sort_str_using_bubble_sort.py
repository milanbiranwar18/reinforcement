# Method #4: Using Bubble sort
# Approach
# Using Bubble sort
#
# Algorithm
# 1. Convert the string into a list of characters.
# 2. Use the bubble sort algorithm to sort the list.
# 3. Join the sorted list to form a string.

def sort_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)


def sort_str(a_str):
    chars = list(a_str)
    for i in range(len(chars)-1, 0, -1):
        for j in range(i):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)


if __name__ == '__main__':
    s = "geekforgeeks"
    print("Original string:", s)
    print("String after sorting:", sort_string(s))
    print()

    print(sort_str('geekforgeeks'))
