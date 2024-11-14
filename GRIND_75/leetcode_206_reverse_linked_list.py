# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive Trivial Solution


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def rev(head, prev=None):
            if not head:
                return prev
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            return rev(head, prev)
        return rev(head)

# Optimal Solution


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev = None
        while (head):
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev


l1 = ListNode(1)
l2 = ListNode(2)
l4 = ListNode(4)
l1.next = l2
l2.next = l4

s = Solution()
s.reverseList(l1)
