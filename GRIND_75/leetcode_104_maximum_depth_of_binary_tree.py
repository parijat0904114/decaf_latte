# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Recursive Approach


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


# DFS Iterative Approach


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, level = stack.pop()
            depth = max(depth, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return depth


# BFS Approach


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)])
        depth = 0
        while queue:
            node, level = queue.popleft()
            depth = max(depth, level)
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
        return depth


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
s = Solution()
print(s.maxDepth(n1))
