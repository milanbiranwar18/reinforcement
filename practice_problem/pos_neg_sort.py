# #1.Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.
#
# Examples
# pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
#
# pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
#
# pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
#
# pos_neg_sort([]) ➞ []
#
# Notes
# If given an empty list, you should return an empty list.
# Integers will always be either positive or negative (0 isn't included in the tests).

def pos_neg_sort(a_list):
    b_list = []
    # for i in range(len(a_list)-1, 0, -1):
    #     for j in range(i):
    #         if (a_list[j] > a_list[j+1]) and a_list[j+1] is abs(a_list[j+1]):
    #             temp = a_list[j]
    #             a_list[j] = a_list[j+1]
    #             a_list[j+1] = temp

    b_list = [a_list[i] for i in range(len(a_list)) if a_list[i] >= 0]

    for i in range(len(b_list)-1, 0, -1):
        for j in range(i):
            if b_list[j] > b_list[j+1]:
                temp = b_list[j]
                b_list[j] = b_list[j+1]
                b_list[j+1] = temp

    j = 0
    for i in range(len(a_list)):
        if a_list[i] >= 0:
            a_list[i] = b_list[j]
            j += 1

    return a_list


if __name__ == '__main__':
    print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))
    print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))
    print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))