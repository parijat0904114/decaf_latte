# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# r = TreeNode(1)
# t1 = TreeNode(2)
# t2 = TreeNode(3)
# r.left = t1
# r.right = t2

# s = Solution()
# print(s.invertTree(r))
