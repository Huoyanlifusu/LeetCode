#递归
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
#迭代
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        stack = []
        stack.append(root)
        while stack:
            node = stack[-1]
            stack.pop()
            if node:
                nums.append(node.val)
            else:
                continue
            stack.append(node.left)
            stack.append(node.right)
        nums.reverse()
        return nums
