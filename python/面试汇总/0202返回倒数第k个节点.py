# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        cur_left, cur_right = head, head
        while k:
            k -= 1
            cur_right = cur_right.next
        while cur_right:
            cur_left = cur_left.next
            cur_right = cur_right.next
        return cur_left.val