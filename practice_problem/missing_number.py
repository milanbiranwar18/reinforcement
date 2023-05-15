# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and
# loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
# Example:
# Input: nums = [1,2,2,4]     Output: [2,3]
# Input: nums = [1,1]         Output: [1,2]


def missing_num(a_list):
    b_list = []
    c_list = []
    for i in a_list:
        if a_list.count(i) > 1 and i not in b_list:
            b_list.append(i)
            c_list.append(i)
        elif i not in b_list:
            c_list.append(i)
    # print(c_list)
    for j in b_list:
        if j+1 not in c_list:
            a = j+1
            b_list.append(a)
    return b_list


if __name__ == '__main__':
    print(missing_num([1,2,2,4]))
    # print(missing_num([1,1]))