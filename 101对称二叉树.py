class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if left and not right: return False
            if right and not left: return False
            if not left and not right: return True
            if left.val != right.val: return False
            return compare(left.left, right.right) and compare(left.right, right.left)
        
        return compare(root.left, root.right)
