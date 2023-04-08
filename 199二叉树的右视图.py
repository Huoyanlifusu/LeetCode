class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []
        if root: queue.append(root)
        while queue:
            size = len(queue)
            path = []
            while size:
                node = queue.pop(0)
                path.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                size -= 1
            result.append(path[0])
        return result
