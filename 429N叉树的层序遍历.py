class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = []
        result = []
        if root: queue.append(root)
        while queue:
            size = len(queue)
            path = []
            while size:
                node = queue.pop(0)
                for child in node.children:
                    if child:
                        queue.append(child)
                path.append(node.val)
                size -= 1
            result.append(path)
        return result
