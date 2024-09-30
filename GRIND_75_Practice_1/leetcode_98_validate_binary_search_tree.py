# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate_bst(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (validate_bst(node.left, left, node.val) and
                    validate_bst(node.right, node.val, right))

        return validate_bst(root, -float('inf'), float('inf'))


n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3

s = Solution()
print(s.isValidBST(n1))
