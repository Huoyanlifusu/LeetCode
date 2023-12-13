# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def digui(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2:
                return True
            elif root2 and not root1:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return digui(root1.left, root2.left) and digui(root1.right, root2.right)
        
        def search(A, B):
            if B == None or A == None:
              return False
            return digui(A, B) or search(A.left, B) or search(A.right, B)
            
        return search(A, B)