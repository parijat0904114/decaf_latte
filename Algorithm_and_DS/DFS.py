class Node():
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.children = []

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n1.children = [n2, n3]
n3.children = [n4, n5]
n4.children = [n6, n7, n8]

traversal_list = []
def dfs(node):
    if node.visited:
        return
    traversal_list.append(node.value)
    node.visited = True

    for child in node.children:
        dfs(child)        

dfs(n1)
print(traversal_list)
