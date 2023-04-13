# #Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
# functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and
# is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
# (double-ended queue) as long as you use only a queue's standard operations.
#
#
# Example 1:
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#


class MyStack(object):

    def __init__(self):
        self.a_list = []
        self.b_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a_list.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.a_list) > 1:
            self.b_list.append(self.a_list.pop(0))
        l_element = self.a_list.pop(0)
        self.a_list, self.b_list = self.b_list, self.a_list
        return l_element

    def top(self):
        """
        :rtype: int
        """
        while len(self.a_list) > 1:
            self.b_list.append(self.a_list.pop(0))
        l_element = self.a_list.pop(0)
        self.b_list.append(l_element)
        self.a_list, self.b_list = self.b_list, self.a_list
        return l_element

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.a_list) == 0 and len(self.b_list) == 0


if __name__ == '__main__':

    obj = MyStack()
    obj.push(10)
    param_2 = obj.pop()
    print(param_2)

    # param_3 = obj.top()
    # print(param_3)
    #
    # param_4 = obj.empty()
    # print(param_4)
