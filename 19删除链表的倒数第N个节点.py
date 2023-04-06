#快慢指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = n + 1
        dummyHead = ListNode()
        dummyHead.next = head
        fast = dummyHead
        slow = dummyHead
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        while slow and fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyHead.next    
