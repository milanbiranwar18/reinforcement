# #Elavarasu A08:35
# Given a singly-linked list of integers, rearrange its nodes to be sorted in increasing order.
#
# Input : 6 —> 3 —> 4 —> 8 —> 2 —> 9 —> None
# Output: 2 —> 3 —> 4 —> 6 —> 8 —> 9 —> None
#
# Input : 9 —> -3 —> 5 —> -2 —> -8 —> -6 —> None
# Output: -8 —> -6 —> -3 —> -2 —> 5 —> 9 —> None


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def print_linked_list(self):
        a_list = []
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                a_list.append(n.data)
                n = n.ref
        print()
        for i in range(len(a_list)-1, 0, -1):
            for j in range(i):
                if a_list[j] > a_list[j+1]:
                    a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

        for i in a_list:
            print(i, '-->', end=' ')


if __name__ == '__main__':
    obj = LinkedList()
    obj.add_begin(9)
    obj.add_begin(2)
    obj.add_begin(8)
    obj.add_begin(4)
    obj.add_begin(3)
    obj.add_begin(6)
    obj.print_linked_list()
    print()
    print()
    obj1 = LinkedList()
    obj1.add_begin(-6)
    obj1.add_begin(-8)
    obj1.add_begin(-2)
    obj1.add_begin(5)
    obj1.add_begin(-3)
    obj1.add_begin(9)
    obj1.print_linked_list()
    # 9 — > -3 — > 5 — > -2 — > -8 — > -6

