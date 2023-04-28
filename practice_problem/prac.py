def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    a_list = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             a_list.append(i)
    #             a_list.append(j)
    # return a_list
    b_list = [a_list.append(i) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]


if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))