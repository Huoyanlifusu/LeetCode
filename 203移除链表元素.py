#迭代法
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next
        if head is None:
            return head
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
                
        
        return head
