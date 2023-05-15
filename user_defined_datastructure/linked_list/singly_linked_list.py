class Node:
    def __init__(self, data):
        self.data = data         # initialising fields of the nodes
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None    # in empty linked list node is none

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)        # creating object of Node  class to create Node with ref. None value
        new_node.ref = self.head     # ref. which is store in head storing that ref. to new node  After this new node become the first node of the linked list
        self.head = new_node         # storing ref of new node in head

    def add_end(self, data):
        new_node = Node(data)        # creating node
        if self.head is None:        # checking linked list is empty or not
            self.head = new_node     # if linked list is empty storing ref of new node to head
        else:
            n = self.head            # Whatever the ref stored in head that assigning to n now n is first node
            while n.ref is not None:    # using while loop to go to last node
                n = n.ref
            print()
            n.ref = new_node            # changing the reference of the last node to newly created node

    # def travers(self, data):
    #     new_node = Node(data)  # creating node
    #     if self.head is None:  # checking linked list is empty or not
    #         self.head = new_node
    #     else:
    #         n = self.head
    #         while n is not None:
    #             if n.ref is None:
    #                 return n
    #             n = n.ref
    #
    # def add_end(self, data):
    #     new_node = Node(data)        # creating node
    #     if self.head is None:        # checking linked list is empty or not
    #         self.head = new_node     # if linked list is empty storing ref of new node to head
    #     else:
    #         obj = self.travers()
    #         obj.ref = new_node            # changing the reference of the last node to newly created node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:          # checking n.data is equal to x or not
                break
            n = n.ref              # To go in next Node reassigning n with ref of node, now n is next node
        if n is None:
            print("Node is not present in linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref     # storing ref of existing node to new node
            n.ref = new_node         # storing new node ref to existing node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:      # if we add new node before first node
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head                # if we add new node before second third or last node
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:            # if x is not present in linked list
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_if_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty so can't delete node")
        else:
            self.head = self.head.ref      # assigning the ref of next node to the head means to first node

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty so can't delete node")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None                # assigning none value to second last nodes ref

    def delete_by_value(self, x):
        if self.head is None:
            print("Can't delete linked list is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref = n.ref.ref


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add_begin(10)
    linked_list.add_begin(20)
    linked_list.add_begin(30)
    linked_list.add_begin(40)
    # linked_list.add_after(200, 10)
    linked_list.add_before(102, 40)
    linked_list.add_begin(30)
    linked_list.add_end(1000)
    # linked_list.insert_if_empty(10)
    # linked_list.insert_if_empty(20)
    # linked_list.delete_begin()
    # linked_list.delete_end()
    # linked_list.delete_by_value(200)
    linked_list.print_linked_list()
