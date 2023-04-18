# #404. Sum of Left Leaves
# Easy
# 4.4K
# 276
# Companies
# Given the root of a binary tree, return the sum of all left leaves.
#
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:
#
# Input: root = [1]
# Output: 0

def sum_of_left_leaves(a_list):
    pass
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = 0
        while root:
            if root.left:
                pre, isleft = root.left, True
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    if pre == root.left and not pre.left:
                        a = a+pre.left
                    root = root.right
            else:
                root = root.right
        return a


if __name__ == '__main__':
    obj = TreeNode()
    obj1 = Solution()
    # obj1.sumOfLeftLeaves([3,9,20,None,None,15,7])
    # left_leaves([3,9,20,None,None,15,7])
