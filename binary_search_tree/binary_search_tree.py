# 1) Full Binary Tree - It contains 0 or 2 child only. It will not contain 1 child
# 2) Complete Binary Tree - It contains 2 child in each level on any level
# 3) Perfect Binary Tree - It should contain 2 child with same leaf node level or on same level
# 4) Balanced Binary Tree - If deff of height of left subtree and right subtree is 1 or 0 then it is balanced B. T.
# 5) pathological Binary Tree - It contains only one child node in one side only

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:  # for ignoring duplicate data
            return
        # if self.key >= data: # for inserting duplicate values
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        if data < self.key:
            # if self.lchild is not None:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")

    # Traversal method
    def pre_order(self):   # root key / left subtree / right subtree
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    # Traversal method
    def in_order(self):  # left subtree/ root / right subtree
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.pre_order()

    # Traversal method
    def post_order(self):  # left / right / root
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=" ")

    def delete(self, data):
        if self.key is None:
            print("Tree is empty")
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)


if __name__ == '__main__':
    # root = BST(None)
    # print(root.key)
    # print(root.lchild)
    # print(root.rchild)
    #
    # root.lchild = BST(5)
    # print(root.key)
    # print(root.lchild)
    # print(root.rchild)
    # print(root.lchild.key)
    # print(root.lchild.lchild)
    # print(root.lchild.rchild)

    root = BST(None)
    list1 = [20, 4, 30, 4, 1, 5, 6]
    for i in list1:
        root.insert(i)

    # root.search(4)
    # root.search(200)

    print("Pre-Order")
    root.pre_order()
    root.delete(20)
    print("After deleting")
    root.pre_order()


    # print()
    # print("In-Order")
    # root.in_order()
    #
    # print()
    # print("Post-Order")
    # root.post_order()
