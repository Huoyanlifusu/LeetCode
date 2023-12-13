# 深搜 排列组合
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        tmp = []
        n = len(nums)
        def dfs(i):
            if i == n:
                ans.append(list(tmp))
                return
            dfs(i+1)

            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
        
        dfs(0)
        return ans