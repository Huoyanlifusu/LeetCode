# 后序遍历
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backsearch(cur, path, result):
            if not cur.left and not cur.right:
                path.append(cur.val)
                result.append("->".join(list(map(str, path))))
                return result
            path.append(cur.val)
            if cur.left:
                result = backsearch(cur.left, path, result)
                path.pop()
            if cur.right:
                result = backsearch(cur.right, path, result)
                path.pop()
            return result
        if root:
            res = backsearch(root, [], [])
            return res
        else:
            return []
