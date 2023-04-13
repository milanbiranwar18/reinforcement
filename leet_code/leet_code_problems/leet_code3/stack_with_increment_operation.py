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


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.a_list = []
        self.b_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.a_list) < self.maxSize:
            self.a_list.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if len(self.a_list) == 0:
            return -1
        else:
            self.a_list.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        # a = [self.a_list[i] + val for i in range(k) if len(self.a_list) > i]
        # return a
        for i in range(k):
            if len(self.a_list) > i:
                new_ele = self.a_list[i] + val
                self.a_list.pop(i)
                self.a_list.insert(i, new_ele)


    def print_stack(self):
        return self.a_list

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


if __name__ == '__main__':
    obj = CustomStack(3)
    obj.push(1)
    print(obj.print_stack())
    obj.push(2)
    print(obj.print_stack())
    obj.pop()
    print(obj.print_stack())
    obj.push(2)
    print(obj.print_stack())
    obj.push(3)
    print(obj.print_stack())
    obj.push(4)
    print(obj.print_stack())
    print()

    obj.increment(5, 100)
    print(obj.print_stack())
    obj.increment(2, 100)
    print(obj.print_stack())
    obj.pop()
    print(obj.print_stack())
    obj.pop()
    print(obj.print_stack())
    obj.pop()
    print(obj.print_stack())

    print(obj.pop())

    # print(obj.print_stack())

