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
