# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root.val


s = Solution()
r = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
r.left = n1
r.right = n2
print(s.invertTree(r))
