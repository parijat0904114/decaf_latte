class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.revstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.flip()
        return self.revstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.flip()
        return self.revstack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return max(len(self.stack), len(self.revstack)) == 0

    def flip(self):
        if self.revstack:
            return
        while self.stack:
            self.revstack.append(self.stack.pop())


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.peek())
print(queue.peek())
print(queue.empty())
queue.pop()
queue.pop()
print(queue.empty())
