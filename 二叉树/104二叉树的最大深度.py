class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def backsearch(cur, count):
            if cur == None:
                return count
            return max(backsearch(cur.left, count+1), backsearch(cur.right, count+1))
        ans = backsearch(root, 0)
        return ans
