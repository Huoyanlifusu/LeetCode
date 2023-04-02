#后序遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = []
        stack.append(root)
        def backsearch(cur, stack):
            if not cur:
                return
            if cur.left:
                stack.append(cur.left)
                backsearch(cur.left, stack)
            if cur.right:
                stack.append(cur.right)
                backsearch(cur.right, stack)
            return len(stack)
        return backsearch(root, stack)
