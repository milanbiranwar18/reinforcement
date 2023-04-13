# #You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has
# the same maximum capacity.
#
# Implement the DinnerPlates class:
#
# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
# void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
# int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns
# -1 if all the stacks are empty.
# int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from
# that stack or returns -1 if the stack with that given index is empty.
#
#
# Example 1:
#
# Input
# ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack",
# "pop", "pop", "pop", "pop", "pop"]
# [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
# Output
# [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
#
# Explanation:
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 4.  The stacks are now:   1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 3.  The stacks are now:   1
#                                                         ﹈
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
#

# #Design a stack that supports increment operations on its elements.
#
# Implement the CustomStack class:
#
# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in
# the stack, increment all the elements in the stack.

# Example 1:
#
# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack stk = new CustomStack(3); // Stack is Empty []
# stk.push(1);                          // stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.push(3);                          // stack becomes [1, 2, 3]
# stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
# stk.increment(5, 100);                // stack becomes [101, 102, 103]
# stk.increment(2, 100);                // stack becomes [201, 202, 103]
# stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
# stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
# stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
# stk.pop();                            // return -1 --> Stack is empty return -1.
#

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.a_list = []
        self.b_list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.a_list) < self.capacity:
            self.a_list.append(val)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.a_list) == 0:
            return -1
        else:
            self.a_list.pop()

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """

    def print_stack(self):
        return self.a_list

# class CustomStack(object):
#
#     def __init__(self, maxSize):
#         """
#         :type maxSize: int
#         """
#         self.maxSize = maxSize
#         self.a_list = []
#         self.b_list = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         if len(self.a_list) < self.maxSize:
#             self.a_list.append(x)
#
#
#     def pop(self):
#         """
#         :rtype: int
#         """
#         if len(self.a_list) == 0:
#             return -1
#         else:
#             self.a_list.pop()
#
#     def increment(self, k, val):
#         """
#         :type k: int
#         :type val: int
#         :rtype: None
#         """
#         # a = [self.a_list[i] + val for i in range(k) if len(self.a_list) > i]
#         # return a
#         for i in range(k):
#             if len(self.a_list) > i:
#                 new_ele = self.a_list[i] + val
#                 self.a_list.pop(i)
#                 self.a_list.insert(i, new_ele)
#
#
#     def print_stack(self):
#         return self.a_list

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


if __name__ == '__main__':
    obj = DinnerPlates(2)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)

    print(obj.print_stack())

