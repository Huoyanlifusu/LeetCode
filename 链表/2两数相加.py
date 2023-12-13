#递归
class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val
        if l1.val >= 10:
            l1.next = self.addTwoNumbers(l1.next, ListNode(1))
            l1.val %= 10

        
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        
        return l1
