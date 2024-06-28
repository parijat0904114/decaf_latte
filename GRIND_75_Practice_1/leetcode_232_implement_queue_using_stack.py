class MyQueue(object):

    def __init__(self):
        self.stack, self.stack_reverse = [], []

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
        return self.stack_reverse.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.flip()
        return self.stack_reverse[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack and not self.stack_reverse

    def flip(self):
        if not self.stack_reverse:
            while self.stack:
                self.stack_reverse.append(self.stack.pop())


# obj = MyQueue()
# obj.push(2)
# obj.push(3)
# obj.push(4)
# print(obj.empty())
# print(obj.peek())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.empty())