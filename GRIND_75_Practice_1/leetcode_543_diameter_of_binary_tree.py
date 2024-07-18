# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    max_diameter = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left:
            left_diameter = 1 + self.diameterOfBinaryTree(root.left)
        if root.right:
            right_diameter = 1 + self.diameterOfBinaryTree(root.right)
        if left_diameter + right_diameter > self.max_diameter:
            self.max_diameter = left_diameter + right_diameter
        return self.max_diameter       


root = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5

s = Solution()
print(s.diameterOfBinaryTree(root))