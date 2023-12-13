# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkSymmetricTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def digui(left, right):
            if left == right == None: return True
            if left == None or right == None: return False
            if left.val != right.val: return False
            return digui(left.left, right.right) and digui(left.right, right.left)

        if root == None or (root.left == root.right == None):
            return True
        
        return digui(root.left, root.right)