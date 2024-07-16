# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left),
                   1 + self.maxDepth(root.right))

# t1 = TreeNode(3)
# t2 = TreeNode(9)
# t3 = TreeNode(20)
# t4 = TreeNode(15)
# t5 = TreeNode(7)
# t1.left = t2
# t1.right = t3
# t3.left = t4
# t3.right = t5

# s = Solution()
# print(s.maxDepth(t1))