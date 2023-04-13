# #233. Number of Digit One
# Hard
# 1.1K
# 1.3K
# Companies
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: 6
# Example 2:
#
# Input: n = 0
# Output: 0
#

def count_digit_one(num):
    count = 0
    # for num in range(1, n+1):
    while num > 0:
        if num==1:
            count+=1
        # elif num%2==:
        #     print(num%2)
        #     count+=1

        num = num//10

    print(count)


if __name__ == '__main__':
    print(count_digit_one(13))