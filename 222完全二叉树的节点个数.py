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
#判断满树
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getNum(node):
            if not node: return 0
            left = node.left
            right = node.right
            lNum, rNum = 0, 0
            while left:
                lNum += 1
                left = left.left
            while right:
                rNum += 1
                right = right.right
            if lNum == rNum: return pow(2, lNum+1) - 1
            lNum = getNum(node.left)
            rNum = getNum(node.right)
            result = lNum + rNum + 1
            return result
        return getNum(root)
