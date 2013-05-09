

class Node(object):
    """docstring for Node"""

    __slots__ = ('data', 'next')
    
    def __init__(self, data, next):
        self.data = data
        self.next = next
    

class Stack(object):
    """docstring for Stack"""

    def __init__(self):
        self.head = Node(None, None)    # sentinel node
        self.len = 0

    def __len__(self):
        return self.len

    def push(self, data):
        self.head = Node(data, self.head)
        self.len += 1

    def pop(self):
        if not self.len:
            raise IndexError
        result = self.head
        self.head = self.head.next
        self.len -= 1
        return result.data

    def reverse(self):
        if self.len < 2:
            # reverse would do nothing
            return

        prev = self.head
        pointer = self.head.next
        tail = self.head
        while pointer.next is not None:
            # temp         <- pointer.next
            # pointer.next <- prev
            # prev         <- pointer
            # pointer      <- temp
            pointer.next, prev, pointer = prev, pointer, pointer.next
        self.head = prev
        # reassigned the sentinel to the new end
        tail.next = pointer

class Queue(object):
    """docstring for Queue"""

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def queue(self, data):
        self.inbox.push(data)

    def dequeue(self):
        if not self.outbox: 
            self.outbox, self.inbox = self.inbox, self.outbox
            self.outbox.reverse()
        try:
            return self.outbox.pop()
        except IndexError:
            raise IndexError, "Queue is empty."


if __name__ == "__main__":
    q = Queue()
    q.queue(1)
    print q.dequeue()