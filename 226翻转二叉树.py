#层序遍历法
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        if root != None: queue.append(root)
        while queue:
            size = len(queue)
            while size > 0:
                size -= 1
                node = queue.pop()
                if not node:
                    continue
                if node.left or node.right:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)
        return root
#递归遍历
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def digui(cur):
            if not cur:
                return
            if cur.left or cur.right:
                cur.left, cur.right = cur.right, cur.left
                digui(cur.left)
                digui(cur.right)
        if root != None: digui(root)
        return root
