class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
            queue = []
            count = 0
            if root: queue.append(root)
            else: return count
            while queue:
                l = len(queue)
                count += 1
                while l > 0:
                    l -= 1
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if not node.left and not node.right:
                        return count
