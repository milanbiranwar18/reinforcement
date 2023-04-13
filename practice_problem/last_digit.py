# #Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the
# last digit of c. Check the examples below for an explanation.
#
# Examples
# last_dig(25, 21, 125) ➞ True
# # The last digit of 25 is 5, the last digit of 21 is 1, and the last
# # digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# # to the last digit of 125(5).
#
# last_dig(55, 226, 5190) ➞ True
# # The last digit of 55 is 5, the last digit of 226 is 6, and the last
# # digit of 5190
# last_dig(12, 215, 2142) ➞ False
# # The last digit of 12 is 2, the last digit of 215 is 5, and the last
# # digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
# # not equal to the last digit of 2142(2).
#
def last_dig(num1, num2, num3):
    a = num1 % 10
    b = num2 % 10
    c = num3 % 10
    d = (a*b) % 10
    if d == c:
        return True
    return False


if __name__ == '__main__':
    print(last_dig(25, 21, 125))
    print(last_dig(55, 226, 5190))
    print(last_dig(12, 215, 2142))