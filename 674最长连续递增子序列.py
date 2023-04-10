#动态规划
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i-1]+1, dp[i])
        
        result = max(dp)
        return result
