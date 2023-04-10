# Queue using LinkList

# from linklist_demo import Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self):
        self.head = None

    def enque(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.head == None:
            print('Queue is empty')
        else:
            temp = self.head
            previous = None
            while temp.next != None:
                previous, temp = temp, temp.next
            data = temp.data
            previous.next = None
            return data

    def display(self):
        if self.head == None:
            print('Queue is empty')
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next


if __name__ == "__main__":
    obj = QueueUsingLinkedList()
    obj.enque("abc")
    obj.enque("bcd")
    obj.enque("def")
    obj.dequeue()
    obj.display()