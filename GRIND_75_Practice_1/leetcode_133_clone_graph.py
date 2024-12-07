from collections import deque
# Definition for a Node.


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            current_node = q.popleft()

            for nei in current_node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei)
                    q.append(nei)
                old_to_new[current_node].neighbors.append(old_to_new[nei])
        return old_to_new[node]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s = Solution()
s.cloneGraph(n1)
