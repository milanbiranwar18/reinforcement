class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Stack:
    def __init__(self):
        self.head = None

    def print_stack(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--", end=" ")
                n = n.ref

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            # popped_node = self.head
            self.head = self.head.ref
            # popped_node.ref = None
            # print(popped_node.data)

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        else:
            print(self.head.data)

    def size(self):
        count = 0
        n = self.head
        while n:
            count += 1
            n = n.ref
        print(count)


if __name__ == '__main__':
    st = Stack()
    st.push(40)
    st.push(30)
    st.push(20)
    st.push(10)
    print(st.is_empty())
    st.peek()
    st.size()
    st.pop()
    st.print_stack()



