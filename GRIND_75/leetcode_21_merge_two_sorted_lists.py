# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = runner = ListNode()

        while (list1 and list2):
            if list1.val < list2.val:
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next
            runner = runner.next

        runner.next = list1 or list2

        return dummy.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l3
l2.next = l4

s = Solution()
print(s.mergeTwoLists(l1, l2))
