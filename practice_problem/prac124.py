# Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be
# found in biglst, and in the same order.
#
# Examples:
#
# [4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
# [5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
# [5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered
# sublist of [3, 2, 1, 2, 3].
# Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.
#
# Examples
# is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True
#
# is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False
#
# is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
# Notes
# Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst.


def is_ord_sub(a_list, b_list):
    a = []

    for i in range(len(a_list)):
        # a = a_list[i] - a_list[i+1]
        for j in range(len(b_list)):
            # b = b_list[j] - b_list[j+1]
            # if a_list[i] == b_list[j] and a == b:
            if a_list[i] == b_list[j]:
                a.append(a_list[i])
    print(a)
    if a_list == a:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]))
    print(is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]))
    print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]))
    print(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]))