class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def move(root):
            tmp = root
            pre = root
            while root.next:
                pre = root
                root = root.next
            pre.next = None
            root.next = tmp
            return root
        if not head or not head.next: return head

        cur = head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next

        k %= count
        
        root = head
        while k:
            k -= 1
            root = move(root)
        return root
