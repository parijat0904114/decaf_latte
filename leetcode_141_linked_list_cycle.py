# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr_fast = head
        ptr_slow = head
        while ptr_fast is not None and ptr_fast.next is not None:
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next

            if ptr_fast == ptr_slow:
                return True
        return False


# s = Solution()
# l1 = ListNode(3)
# l2 = ListNode(2)
# l3 = ListNode(0)
# l4 = ListNode(-4)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l2
# print(s.hasCycle(l1))
