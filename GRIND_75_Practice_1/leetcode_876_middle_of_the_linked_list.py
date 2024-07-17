# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast_ptr = slow_ptr = head
        while (fast_ptr.next and fast_ptr.next.next):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        if fast_ptr.next:
            return slow_ptr.next
        else:
            return slow_ptr

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

s = Solution()
print(s.middleNode(l1))