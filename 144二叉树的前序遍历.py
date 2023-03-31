//递归
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        def digui(cur, nums):
            if cur == None:
                return
            nums.append(cur.val)
            digui(cur.left, nums)
            digui(cur.right, nums)
        digui(root, nums)
        return nums
