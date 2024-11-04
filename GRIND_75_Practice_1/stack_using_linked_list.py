class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            print("Empty Stack")
        else:
            self.head = self.head.next

    def top(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        else:
            print(self.head.val)

    def print_stack(self):
        curr = self.head
        while (curr):
            print(curr.val, "->")
            curr = curr.next
        print("None")

    def is_empty(self):
        return self.head is None


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.top()
s.pop()
s.print_stack()
s.top()
