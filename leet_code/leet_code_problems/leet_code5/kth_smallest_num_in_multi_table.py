# #668. Kth Smallest Number in Multiplication Table
# Hard
# 1.9K
# 52
# Companies
# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat
# where mat[i][j] == i * j (1-indexed).
#
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
#
#
#
# Example 1:
#
#
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.
# Example 2:
#
#
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.

def smallest_num(m, n, x):
    count = 0
    for i in range(1, m + 1):
        count += min(x // i, n)
    return count


if __name__ == '__main__':

    print(smallest_num(3,3,5))

