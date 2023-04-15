# 求高度都是后序遍历
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeihgt(cur):
            if cur == None: return 0
            leftHeight = getHeihgt(cur.left)
            rightHeight = getHeihgt(cur.right)
            if leftHeight == -1 or rightHeight == -1: return -1
            if abs(leftHeight - rightHeight) > 1: return -1
            return (1 + max(leftHeight, rightHeight))
        if getHeihgt(root) == -1:
            return False
        else:
            return True
