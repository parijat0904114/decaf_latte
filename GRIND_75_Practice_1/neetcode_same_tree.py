# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        if not (p and q):
            return False
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)
        return True
