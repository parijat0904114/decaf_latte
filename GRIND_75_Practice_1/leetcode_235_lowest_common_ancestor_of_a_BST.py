# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val> q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# t1 = TreeNode(6)
# t2 = TreeNode(2)
# t3 = TreeNode(8)
# t4 = TreeNode(4)
# t1.left = t2
# t1.right = t3
# t2.right = t4

# s = Solution()
# print(s.lowestCommonAncestor(t1,t2,t3))

# s2 = Solution()
# print(s.lowestCommonAncestor(t2, t2, t4))