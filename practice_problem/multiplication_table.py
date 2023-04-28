# #Your task, is to create N x N multiplication table, of size n provided in parameter.
#
# For example, when n is 5, the multiplication table is:
#
# 1, 2, 3, 4, 5
# 2, 4, 6, 8, 10
# 3, 6, 9, 12, 15
# 4, 8, 12, 16, 20
# 5, 10, 15, 20, 25
# This example will result in:
#
# [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
# Examples
# multiplication_table(1) ➞ [[1]]
#
# multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def multiplication_table(n):
    a_list = []
    for i in range(1, n+1):
        b_list = []
        for j in range(1, n+1):
            b_list.append(j*i)
        a_list.append(b_list)
    return a_list


if __name__ == '__main__':
    print(multiplication_table(5))
    print(multiplication_table(1))
    print(multiplication_table(3))
