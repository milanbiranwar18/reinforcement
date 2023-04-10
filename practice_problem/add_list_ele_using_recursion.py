# Create a function that sums up all the elements in the list recursively. The use of the sum() built-in function is
# not allowed, thus, the approach is recursive.
#
# Examples
# recur_add([1, 2, 3, 4, 10, 11]) ➞ 31
#
# recur_add([-3, 4, 11, 10, 21, 32, -9]) ➞ 66
#
# recur_add([-21, -7, 19, 3, 4, -8]) ➞ -10


def sums_of_ele(a_list):
    if len(a_list) == 0:
        return 0
    else:
        return a_list[0] + sums_of_ele(a_list[1:])


if __name__ == '__main__':
    print(sums_of_ele([1, 2, 3, 4, 10, 11]))
    print(sums_of_ele([-3, 4, 11, 10, 21, 32, -9]))
    print(sums_of_ele([-21, -7, 19, 3, 4, -8]))