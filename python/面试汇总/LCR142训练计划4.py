# Definition for singly-linked list.

# 本质上是链表排序题目
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def trainningPlan(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        q = ListNode()
        head = q
        while l1 or l2:
            if not l1:
                q.next = l2
                q = q.next
                l2 = l2.next
            elif not l2:
                q.next = l1
                q = q.next
                l1 = l1.next
            elif l1.val <= l2.val:
                q.next = l1
                q = q.next
                l1 = l1.next
            else:
                q.next = l2
                q = q.next
                l2 = l2.next
        return head.next