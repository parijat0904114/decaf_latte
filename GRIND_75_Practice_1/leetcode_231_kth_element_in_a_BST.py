# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Brute Force


# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: Optional[TreeNode]
#         :type k: int
#         :rtype: int
#         """
#         lst = []

#         def dfs(node):
#             if not node:
#                 return
#             lst.append(node.val)
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
#         lst.sort()
#         return lst[k-1]

# Inorder Traversal


# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: Optional[TreeNode]
#         :type k: int
#         :rtype: int
#         """
#         lst = []

#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             lst.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return lst[k-1]

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n3.left = n1
n3.right = n4
n1.right = n2

s = Solution()
print(s.kthSmallest(n1, 1))
