# Create a function that takes a list lst and a number n and returns a list of two integers whose product is that of
# the number n.
#
# Examples
# two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
#
# two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
#
# two_product([100, 12, 4, 1, 2], 15) ➞ None
# Notes
# No duplicates.
# Sort the number.
# Try doing this with 0(n) time complexity.
# The list can have multiple solutions, so return the first match you find.

def product_of_ele_list(a_list, n):

    for i in range(1, len(a_list)):
        val = a_list[i]
        j = i-1
        while j >= 0 and val < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = val

    for i in range(len(a_list)):
        for j in a_list[i:]:
            if a_list[i] * j == n:
                return [a_list[i], j]


if __name__ == '__main__':
    print(product_of_ele_list([1, 2, 3, 4, 13, 5], 39))
    print(product_of_ele_list([11, 2, 7, 3, 5, 0], 55))
    print(product_of_ele_list([100, 12, 4, 1, 2], 15))