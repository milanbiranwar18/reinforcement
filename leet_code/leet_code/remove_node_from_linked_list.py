#You are given the head of a linked list.

# Remove every node which has a node with a strictly greater value anywhere to the right side of it.
#
# Return the head of the modified linked list.
# Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# Example 2:
#
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # n = self.head
        # while n is not None:
        #     if head and head.val < head.val:
        #         return head.next
        #     n = n.next
        # return head

        # for val in head:
        # new_node = ListNode(val)
        # new_node.next = self.head
        # self.head = new_node

        if not head:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head


if __name__ == '__main__':
    obj = Solution()
    head = [5, 2, 13, 3, 8]
    for node in head:
        obj.add_node(node)

    print(obj.removeNodes(head))

