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
        counter = 0
        head_copy = head
        while head:
            counter += 1
            head = head.next
        counter = counter // 2 if counter % 2 == 0 else (counter // 2)
        print(counter)
        print(head_copy.val)
        while counter:
            head_copy = head_copy.next
            counter -= 1
        return head_copy.val


obj = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
print(obj.middleNode(n1))
