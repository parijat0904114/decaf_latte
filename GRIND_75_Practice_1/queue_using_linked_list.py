class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = self.tail = None

    def enque(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def deque(self):
        if self.is_empty():
            print("The queue is empty")

        else:
            self.head = self.head.next

    def is_empty(self):
        return self.head is None

    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.val

    def print_queue(self):
        curr = self.head

        while (curr):
            print(curr.val)
            curr = curr.next


q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
print(q.front())
q.print_queue()
q.deque()
q.print_queue()
