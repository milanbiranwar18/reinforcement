# TODO 1. Write a Python program to create a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, '--', end=" ")
                n = n.ref

    def add_data(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    # TODO 2. Write a Python program to find the size of a singly linked list.
    def size(self):
        count = 0
        n = self.head
        while n:
            count += 1
            n = n.ref
        print(count)

    # TODO 3. Write a Python program to search a specific item in a singly linked list and return true if the item is
    #   found otherwise return false.
    def search_item(self, x):
        n = self.head
        while n is not None:
            if x == n.data:
                return True
            n = n.ref
        return False

    # TODO 4. Write a Python program to access a specific item in a singly linked list using index value.
    def search_item_using_index(self, x):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            if (count - 1) == x:
                return n.data
            n = n.ref
        return "Index out of range, please insert valid index."

    # TODO 5. Write a Python program to set a new value of an item in a singly linked list using index value.
    def setting_new_value_using_index(self, data, x):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            if (count - 1) == x:
                new_node = Node(data)
                new_node.ref = self.head
                self.head = new_node
                break
            elif count == x:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                break
            n = n.ref

    # TODO 6. Write a Python program to delete the first item from a singly linked list.
    def delete_first_element(self):
        self.head = self.head.ref

    # TODO 7. Write a Python program to delete the last item from a singly linked list.
    def delete_last_element(self):
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    # TODO 8. Write a Python program to reverse a linked list using iterative methode.
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.ref
            curr.ref = prev
            prev = curr
            curr = next
        self.head = prev

    # TODO 9. Write a Python program to reverse a linked list using recursive methode.
    def reverse_util(self, curr, prev):

        if curr.ref is None:           # If last node mark it head
            self.head = curr
            curr.ref = prev            # Update ref to prev node
            return
        next = curr.ref                # Save curr.ref node for recursive call
        curr.ref = prev                # And update ref
        self.reverse_util(next, curr)  # This function mainly calls reverse_util() with previous as None

    def reverse(self):
        if self.head is None:
            return
        self.reverse_util(self.head, None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_data(10)
    ll.add_data(20)
    ll.add_data(30)
    ll.add_data(40)
    # ll.is_empty()
    ll.print_linked_list()
    print()
    # ll.size()
    # print(ll.search_item(10))
    # print(ll.search_item_using_index(1))
    # ll.setting_new_value_using_index(30, 2)
    # print(ll.search_item_using_index(1))
    # ll.print_linked_list()
    print()
    # ll.delete_first_element()
    # ll.delete_last_element()
    # ll.print_linked_list()
    ll.reverse_list()
    print()
    # ll.reverse()
    ll.print_linked_list()
