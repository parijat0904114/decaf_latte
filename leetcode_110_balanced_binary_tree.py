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
        self.balanced = True

        def height(node):
            if not node:
                return 0

            if not self.balanced:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return self.balanced


# root = TreeNode(1)
# l1 = TreeNode(2)
# l2 = TreeNode(3)
# l3 = TreeNode(4)
# l4 = TreeNode(5)
# l5 = TreeNode(6)
# root.left = l1
# root.right = l2
# l1.left = l3
# l3.left = l4
# l4.left = l5
# s = Solution()
# print(s.isBalanced(root))

"""
Balanced Tree:
Consider the following tree:
    A
   / \
  B   C
 / \   \
D   E   F

Traversal and Balance Check:

1. Starting at the root A, we first visit the left child B.
2. At B, we go deeper into the left child D. D is a leaf node; hence it returns a height of 1.
3. Now at B, we explore the right child E. Like D, E is also a leaf node and returns a height of 1.
4. For B, we compare the heights of D and E. The difference is 0, which is within the balanced limit.
5. B then calculates its height as 1 + max(height of D, height of E) and returns 2 to its parent, A.
6. Now for A, we traverse the right child C.
7. At C, we dive into its only child F. Being a leaf node, F returns a height of 1.
8. C calculates its own height as 1 + height of F and returns 2 to its parent, A.
9. Finally, for the root A, we have the heights of both children B and C as 2. The difference is 0, which again is within balance limits.

Conclusion: The tree is balanced as every node's left and right subtrees' height difference is within 1.
"""

"""
Unbalanced Tree:
Now consider this tree:

    A
   / 
  B   
 / 
D  

Traversal and Balance Check:

1. Starting at the root A, we first visit the left child B.
2. At B, we go deeper into the left child D. D is a leaf node, so it returns a height of 1.
3. B now calculates its own height as 1 + height of D which is 2 and returns this to its parent, A.
4. For A, there is no right child to traverse, so the height for the right subtree is 0.
5. Now, at A, when comparing the heights of its left and right subtrees, we find a difference of 2, which exceeds the balance limit of 1.

Conclusion: The tree is unbalanced since the root node has a left-right subtree height difference greater than 1.
"""
