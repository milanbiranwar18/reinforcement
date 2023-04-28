# #67. Add Binary
# Easy
# 7.9K
# 772
# Companies
# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


def add_binary(a, b):
    # Step 1: Convert binary strings to decimal integers
    a_decimal = int(a, 2)
    b_decimal = int(b, 2)

    # Step 2: Add the decimal integers
    sum_decimal = a_decimal + b_decimal

    # Step 3: Convert the sum back to binary string
    sum_binary = bin(sum_decimal)

    # Step 4: Remove the prefix '0b' from the binary string and return
    return sum_binary[2:]
