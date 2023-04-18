# Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first
# element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the
# nearest whole number.
#
# Examples
# sum_fractions([[18, 13], [4, 5]]) ➞ 2
#
# sum_fractions([[36, 4], [22, 60]]) ➞ 9
#
# sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
# Notes
# Your result should be a number not string.
import math


def fractions_rounded(a_list):
    sum_frac = 0
    for sub_list in a_list:
        frac = sub_list[0]/sub_list[1]
        sum_frac += frac
    return math.floor(sum_frac)


if __name__ == '__main__':
    print(fractions_rounded([[18, 13], [4, 5]]))
    print(fractions_rounded([[36, 4], [22, 60]]))
    print(fractions_rounded([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
