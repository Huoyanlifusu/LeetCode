# 双链表法
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        q = ListNode(-1)
        l1, l2 = p, q
        while head:
            node = ListNode(head.val)
            if head.val >= x:
                q.next = node
                q = q.next
            if head.val < x:
                p.next = node
                p = p.next
            head = head.next
        
        p.next, q.next = l2.next, None
        return l1.next