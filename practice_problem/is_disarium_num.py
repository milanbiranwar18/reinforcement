# "A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.
#
# Examples
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32
#
# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
#
# is_disarium(544) ➞ False
#
# is_disarium(518) ➞ True
#
# is_disarium(466) ➞ False
#
# is_disarium(8) ➞ True
# "

def is_disarium_num(num):
    num_string = str(num)
    a = 1
    b = 0
    for i in num_string:
        c = int(i)**a
        b += c
        a += 1
    if b == num:
        return True
    return False


if __name__ == '__main__':
    num = 466
    res_num = is_disarium_num(num)
    print(res_num)