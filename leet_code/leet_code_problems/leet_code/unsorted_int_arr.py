"""
# Given an unsorted integer array, find all quadruplets (i.e., four elements tuple) having a given sum.
#
# Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 7
# Output: {(0, 1, 2, 4)}
#
# Since the input can contain multiple quadruplets that sum to a given target, the solution should return a set containing
#  all the quadruplets.
#
# Input : nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 20
# Output: {(0, 4, 7, 9), (1, 3, 7, 9), (2, 4, 5, 9)}
# Note: The order of elements doesn't matter in a quadruplet, and any permutation is allowed in the output. For example,
#  the output set can contain quadruplets [9, 1, 7, 3] and [9, 3, 7, 1], but system treats them the same.
"""


def quadruplets(lst, target):
    quadruplet = []
    for i in range(len(lst)):  # 2
        for j in range(i + 1, len(lst)):  # 7
            for k in range(j + 1, len(lst)):  # 4,0,9,5,1
                for l in range(k + 1, len(lst)):  # 0,9,5,1,3
                    quad = (lst[i], lst[j], lst[k], lst[l])
                    if sum(quad) == target:
                        quadruplet.append(quad)
    return quadruplet


if __name__ == '__main__':

    print(quadruplets([2, 7, 4, 0, 9, 5, 1, 3], 7))
    print(quadruplets([2, 7, 4, 0, 9, 5, 1, 3], 20))


