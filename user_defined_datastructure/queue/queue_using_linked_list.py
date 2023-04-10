class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def print_queue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            n = self.front
            while n is not None:
                print(n.data, "--", end=" ")
                n = n.ref

    def enqueue(self, data):
        if self.rear is None:
            self.front = self.rear = Node(data)
        else:
            self.rear.ref = Node(data)
            self.rear = self.rear.ref

    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            to_return = self.front.data
            self.front = self.front.ref
            return to_return

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        cur = self.front
        while cur:
            count += 1
            cur = cur.ref
        return count


if __name__ == '__main__':
    q = Queue()
    q.enqueue(20)
    q.enqueue(10)
    q.enqueue(30)
    q.enqueue(40)
    # q.dequeue()

    print()
    print(q.size())
    print(q.is_empty())
    q.print_queue()


