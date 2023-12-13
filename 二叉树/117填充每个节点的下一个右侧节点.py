class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root: queue.append(root)
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
                if size == 0: node.next = None
                else: node.next = queue[0]
        return root
