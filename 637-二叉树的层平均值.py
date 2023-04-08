class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            avg = float(sum(path))/float(len(path))
            result.append(avg)
        return result
