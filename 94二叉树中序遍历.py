#递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        def digui(cur):
            if not cur:
                return
            digui(cur.left)
            nums.append(cur.val)
            digui(cur.right)
        
        digui(root)
        return nums
#迭代

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                nums.append(cur.val)
                cur = cur.right
        
        
        return nums
