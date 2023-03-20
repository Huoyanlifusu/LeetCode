class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lst = list(s)
        res = []
        def dfs(x):
            if x == len(lst) - 1:
                res.append("".join(lst))
                return
            
            dic = set()

            for i in range(x, len(lst)):
                if lst[i] in dic: continue
                dic.add(lst[i])
                lst[i], lst[x] = lst[x], lst[i]
                dfs(x+1)
                lst[x], lst[i] = lst[i], lst[x]

        dfs(0)
        return res
