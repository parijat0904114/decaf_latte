class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Hashmap(object):
    def __init__(self):
        self.size = 8  # TODO: Dynamic Resizing in future
        self.hash_table = [None] * self.size

    def add(self, lst):
        for value in lst:
            hashed_index = hash(value) % self.size
            if self.hash_table[hashed_index] is None:
                self.hash_table[hashed_index] = Node(value)
            else:
                current = self.hash_table[hashed_index]
                while current.next:
                    current = current.next
                current.next = Node(value)

    def lookup(self, val):
        hashed_index = hash(val) % self.size
        current = self.hash_table[hashed_index]
        while current:
            if val == current.value:
                return 'Found'
            else:
                current = current.next
        return 'Not Found'


d = Hashmap()
d.add(['a', 'b'])
print(d.lookup('c'))
d.add(['c'])
print(d.lookup('b'))
d.add(['e'])
d.add(['j'])
print(d.lookup('c'))
print(d.hash_table)
