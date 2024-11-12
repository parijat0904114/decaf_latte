# Definition for a binary tree node.


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         return max(1 + self.maxDepth(root.left),
#                    1 + self.maxDepth(root.right))


# class Solution(object):
#     def maxDepth(self, root):
#         if not root:
#             return 0
#         left_height = self.maxDepth(root.left)
#         right_height = self.maxDepth(root.right)
#         return 1 + max(left_height, right_height)

# Iterative DFS


# class Solution(object):
#     def maxDepth(self, root):
#         stack = [(root, 1)]
#         depth = 0

#         while stack:
#             node, node_depth = stack.pop()
#             if node:
#                 depth = max(depth, node_depth)
#                 stack.append((node.left, node_depth + 1))
#                 stack.append((node.right, node_depth + 1))
#         return depth

# Breadth First Search


# class Solution(object):
#     def maxDepth(self, root):
#         queue = deque([(root, 1)])
#         depth = 0

#         while queue:
#             node, node_depth = queue.popleft()
#             if node:
#                 depth = max(depth, node_depth)
#                 queue.append((node.left, node_depth + 1))
#                 queue.append((node.right, node_depth + 1))
#         return depth


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
print(s.maxDepth(t1))
