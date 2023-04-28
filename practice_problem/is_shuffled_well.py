# #is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# # 1, 2, 3 appear consecutively
#
# is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# # 9, 8, 7, 6 appear consecutively
#
# is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# # No consecutive numbers appear
# is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# # No consecutive numbers appear
# Notes
# Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being
# properly shuffled (see example #4)).
# You will get numbers from 1-10.


def is_shuffled_well(a_list):
    cons_num = 0
    for i in range(len(a_list)-1):
        a = a_list[i] + 1
        b = a_list[i] - 1
        if a_list[i+1] == a:
            cons_num += 1
            if cons_num >2:
                return False
        elif a_list[i + 1] == b:
            cons_num += 1
            if cons_num > 2:
                return False
    else:
        return True


if __name__ == '__main__':
    print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
    print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
    print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
    print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
