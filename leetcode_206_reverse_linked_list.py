# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next == None:
            return head

        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


# obj = Solution()
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# obj.reverseList(n1)
