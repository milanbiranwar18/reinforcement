#Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
# functions of a normal stack (push, top, pop, and empty).

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

class FrontMiddleBackQueue(object):

    def __init__(self):
        self.a_list = []

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a_list.insert(0, val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        middle = len(self.a_list) // 2
        self.a_list.insert(middle, val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a_list.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        return (self.a_list or [-1]).pop(0)

    def popMiddle(self):
        """
        :rtype: int
        """
        middle = (len(self.a_list) - 1) // 2
        return (self.a_list or [-1]).pop(middle)

    def popBack(self):
        """
        :rtype: int
        """
        return (self.a_list or [-1]).pop()


if __name__ == '__main__':

   obj = FrontMiddleBackQueue()
   print(obj.pushFront(1))
   # print(obj.pushBack(2))
   # print(obj.pushMiddle(3))
   # print(obj.pushMiddle(4))
   obj.pushBack(2)
   obj.pushMiddle(3)
   obj.pushMiddle(4)
   print(obj.popFront())
   print(obj.popMiddle())
   print(obj.popMiddle())
   print(obj.popBack())
   # print(obj.popFront())

