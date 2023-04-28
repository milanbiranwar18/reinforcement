# #94. Binary Tree Inorder Traversal
# Easy
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        a_list = []
        self.in_order(root, a_list)
        return a_list

    def in_order(self, root, a_list):
        if self.left:
            self.in_order(self.left, a_list)
        a_list.append(self.val)
        if self.right:
            self.in_order(self.right, a_list)

        # if self.lchild:
        #     self.lchild.in_order()
        # print(self.key, end=" ")
        # if self.rchild:
        #     self.rchild.pre_order()


if __name__ == '__main__':
    obj = Solution()
    print(obj.right)
    print(obj.val)
    print(obj.left)
    # a = obj.inorderTraversal([1,2,3])
    # print(a)

    # a = [1,2,3]
    # for i in a:
    #     obj.inorderTraversal(i)
    #     print(a)
