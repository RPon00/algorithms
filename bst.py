

from collections import deque

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        prev = None
        node = self.head
        while node is not None:
            prev = node
            if node.value < value:
                node = node.right
            else:
                node = node.left
        else:
            if prev.value < value:
                prev.right = new_node
            else:
                prev.left = new_node

    def delete(self, value):
        pass

    def in_order(self):
        """ Returns a generator representing the in order traversal. """
        node = self.head
        stack = deque()
        while stack or node is not None: 
            if node is not None:
                stack.appendleft(node)
                node = node.left
            else:
                node = stack.popleft()
                yield node.value
                node = node.right

    def pre_order(self):
        node = self.head
        stack = deque()
        while stack or node is not None:
            if node is not None:
                yield node.value
                stack.appendleft(node)
                node = node.left
            else:
                node = stack.popleft()
                node = node.right

    def post_order(self):
        pass


if __name__ == "__main__":
    bst = BST()
    for n in (5,2,7,1,3,9,8):
        bst.insert(n)
    print list(bst.in_order())
    print
    print list(bst.pre_order())