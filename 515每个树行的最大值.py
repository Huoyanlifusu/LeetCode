class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []
        if root: queue.append(root)
        while queue:
            size = len(queue)
            path = []
            while size:
                size -= 1
                node = queue.pop(0)
                path.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(path))
        return result
