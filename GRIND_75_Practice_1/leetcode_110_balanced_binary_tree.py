# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalanced = True
        
        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                self.isBalanced = False
                return 0
            # height is considered maximum_depth for each node.
            return 1 + max(left_height, right_height)

        height(root)
        return self.isBalanced

        

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)

root.left = n1
root.right = n2
n1.left = n3
n3.left = n4
n4.left = n5

s = Solution()
print(s.isBalanced(root))