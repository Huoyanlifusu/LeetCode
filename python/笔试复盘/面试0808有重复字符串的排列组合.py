class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        l = list(S)
        res = []
        def dfs(l, tmp):
            if len(l) == 1:
                if tmp+l[0] not in res:
                    res.append(tmp+l[0])
                return
            n = len(l)
            for i in range(n):
                tmp += l[i]
                dfs(l[:i]+l[i+1:], tmp)
                tmp = tmp[:-1]
        
        dfs(l, "")
        return res
# dfs