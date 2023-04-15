class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        if root != None:
            queue.append(root)
        while len(queue) > 0:
            l = len(queue)
            res = []
            while l > 0:
                l -= 1
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(res) > 0:
                ans.append(res)
        return ans
