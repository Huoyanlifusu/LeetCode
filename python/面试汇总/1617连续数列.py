# 动态规划
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] + list(nums)
        for i in range(1, n+1):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        return max(dp[1:])