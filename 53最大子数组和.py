#贪心算法
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -math.inf
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result: result = count
            if count < 0: count = 0
        return result

#动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        dp.pop(0)
        return max(dp)
