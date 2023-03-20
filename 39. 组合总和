class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates)

        def dfs(candidate, begin, size, path, res, target):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
            for index in range(begin, size):
                dfs(candidate, index, size, path + [candidate[index]], res, target - candidate[index]) 

        res = []
        path = []

        dfs(candidates, 0, size, path, res, target)

        return res
