# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    balanced = True

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def DFS(node):
            if not node:
                return 0
            left_height = DFS(node.left)
            right_height = DFS(node.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False

            return 1 + max(left_height, right_height)

        DFS(root)
        return self.balanced


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n2.left = n3

s = Solution()
print(s.isBalanced(n1))
