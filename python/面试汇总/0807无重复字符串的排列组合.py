# 深度优先搜索
class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        l = list(S)
        def dfs(l, s):
            if l == []:
                res.append(s)
                return
            for i in range(len(l)):
                dfs(l[:i]+l[i+1:], s+l[i])
        dfs(l, "")
        return res