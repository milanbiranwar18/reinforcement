def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums3 = nums1 + nums2
    nums4 = sorted(nums3)
    mid = len(nums4) // 2
    if mid % 2 == 0:
        return (nums4[mid - 1] + nums4[mid]) / 2
    else:
        return nums4[mid]


if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([1,2], [3,4]))