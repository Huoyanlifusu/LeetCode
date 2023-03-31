#递归
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
#迭代
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        nums = []
        stack.append(root)
        while stack:
            node = stack[-1]
            stack.pop()
            if node: nums.append(node.val)
            else: continue
            stack.append(node.right)
            stack.append(node.left)
        return nums
