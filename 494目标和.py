#0-1背包
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == abs(target) else 0
        if sum(nums) < abs(target): return 0
        if (sum(nums)+target) % 2 == 1: return 0
        bagsize = (sum(nums)+target)//2

        dp = [0] * (bagsize+1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bagsize, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        
        return dp[-1]
