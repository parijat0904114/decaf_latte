from collections import deque
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        st = deque([(root)])
        right_view = []

        while st:
            q_len = len(st)
            r = None
            for _ in range(q_len):
                node = st.popleft()
                if node:
                    r = node
                    st.append(node.left)
                    st.append(node.right)
            if r:
                right_view.append(r.val)
        return right_view


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3
t3.right = t4
t2.right = t5

s = Solution()
print(s.rightSideView(t1))
