class LinearSearch():
    """
    """

    def __init__(self, lst, value):
        self.lst = lst
        self.value = value

    def search(self):
        for index, item in enumerate(self.lst):
            if item == self.value:
                return index
        return -1


L = LinearSearch([3, 1, 2, 3, 5], 2)
print(L.search())


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class HashTable(object):
    def __init__(self):
        self.size = 8  # Considering a fixed sized table.
        self.hash_table = [None] * self.size

    def add(self, lst):
        for value in lst:
            hashed_index = hash(value) % self.size
            if not self.hash_table[hashed_index]:
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


d = HashTable()
d.add(['a', 'b'])
print(d.lookup('c'))
d.add(['c'])
print(d.lookup('b'))
d.add(['e'])
d.add(['j'])
print(d.lookup('c'))
print(d.hash_table)
