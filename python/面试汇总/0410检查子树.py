# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkSubTree(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        def isSubTree(root1, root2):
            if root1 == root2 == None: return True
            elif root1 and root2:
                if root1.val == root2.val: return isSubTree(root1.left, root2.left) and isSubTree(root1.right, root2.right)
                else: return False
            else: return False

        def digui(root1, root2):
            if root1 == None:
                return False
            return isSubTree(root1, root2) or digui(root1.left, root2) or digui(root1.right, root2)

        if t2 == None:
            return True
        return digui(t1, t2)