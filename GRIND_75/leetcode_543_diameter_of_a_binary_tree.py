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
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.max_diameter = max(
                self.max_diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        dfs(root)
        return self.max_diameter


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
print(s.diameterOfBinaryTree(n1))
