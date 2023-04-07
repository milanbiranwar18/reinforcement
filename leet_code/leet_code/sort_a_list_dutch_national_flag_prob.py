'''

Given an array containing only 0’s, 1’s, and 2’s, in-place sort it in linear time and using constant space.

Input : [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

'''


def sort_a_list_dutch_prob(nums):
    for i in range(1, len(nums)):
        c_element = nums[i]
        position = i
        while c_element < nums[position - 1] and position > 0:
            nums[position] = nums[position - 1]
            position = position - 1
        nums[position] = c_element
    return nums


if __name__ == '__main__':
    print(sort_a_list_dutch_prob([0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]))