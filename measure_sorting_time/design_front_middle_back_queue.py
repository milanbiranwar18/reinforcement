import math

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None




class FrontMiddleBackQueue(object):

    def __init__(self):
        # self.head = None
        self.a_list = []

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a_list.insert(0, val)
        return self.a_list

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        middle = len(self.a_list)//2
        self.a_list.insert(middle, val)
        # return self.a_list

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a_list.append(val)
        return self.a_list

    def popFront(self):
        """
        :rtype: int
        """
        self.a_list.pop(0)
        return self.a_list

    def popMiddle(self):
        """
        :rtype: int
        """
        middle = (len(self.a_list) - 1) // 2
        # middle = math.floor(midd)
        # print(middle)
        self.a_list.pop(middle)
        return self.a_list

    def popBack(self):
        """
        :rtype: int
        """
        self.a_list.pop()
        return self.a_list


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

if __name__ == '__main__':

   obj = FrontMiddleBackQueue()
   print(obj.pushFront(1))
   print(obj.pushBack(2))
   print(obj.pushMiddle(3))
   print(obj.pushMiddle(4))
   print(obj.popFront())
   print(obj.popMiddle())
   print(obj.popMiddle())
   print(obj.popBack())
   # print(obj.popFront())