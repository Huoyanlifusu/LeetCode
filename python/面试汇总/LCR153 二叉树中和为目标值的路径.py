# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathTarget(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(cur, path):
            if not cur.left and not cur.right:
                if sum(path) + cur.val == target:
                    ans.append(path+[cur.val])
                return
            if cur.left:
                dfs(cur.left, path + [cur.val])
            if cur.right:
                dfs(cur.right, path + [cur.val])
        if root == None:
            return []
        dfs(root, [])
        return ans