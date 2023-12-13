# 搞两个队列 然后对元素按位数相加即可
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        q1, q2 = [], []
        while l1:
            q1.append(l1.val)
            l1 = l1.next
        while l2:
            q2.append(l2.val)
            l2 = l2.next
        
        res = ListNode()
        dummy = res
        jinwei = 0
        while q1 or q2 or jinwei:
            a = q1.pop(0) if q1 else 0
            b = q2.pop(0) if q2 else 0
            cur_sum = a + b + jinwei
            jinwei = cur_sum // 10
            cur_sum = cur_sum % 10

            node = ListNode(cur_sum)
            res.next = node
            res = node
        
        return dummy.next
