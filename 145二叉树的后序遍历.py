class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.digui(root, nums)
        return nums

    def digui(self, cur, nums):
        if not cur:
            return
        self.digui(cur.left, nums)
        self.digui(cur.right, nums)
        nums.append(cur.val)
