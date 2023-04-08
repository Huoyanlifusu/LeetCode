#回溯剪枝

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1 for _ in range(len(nums))]
        def backsearch(nums, i, cache):
            if i < 0: return 0
            if cache[i] != -1: return cache[i]
            res = max(backsearch(nums, i-1, cache), backsearch(nums, i-2, cache)+nums[i])
            cache[i] = res
            return res
        
        return backsearch(nums, len(nums)-1, cache)
#动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)

        for i in range(2, n+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        
        return dp[-1]
