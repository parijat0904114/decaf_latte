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
        dummy_node = ListNode(0)
        current = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy_node.next


# s = Solution()
# l1 = ListNode()
# l2 = ListNode()
# l3 = ListNode()
# l4 = ListNode()
# l5 = ListNode()
# l6 = ListNode()

# l1.val = 1
# l1.next = l2
# l2.val = 2
# l2.next = l3
# l3.val = 3

# l4.val = 4
# l4.next = l5
# l5.val = 5
# l5.next = l6
# l6.val = 6

# print(s.mergeTwoLists(l1, l4))
