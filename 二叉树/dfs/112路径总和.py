class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
#回溯算法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backsearch(cur, path):
            if not cur:
                return sum(path) == targetSum
            path.append(cur.val)
            res1 = backsearch(cur.left, path)
            res2 = backsearch(cur.right, path)
            path.pop()
            return res1 or res2
        
        return backsearch(root, [])
