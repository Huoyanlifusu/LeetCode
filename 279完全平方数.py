#完全背包
import math
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1, int(math.sqrt(n))+1)]

        dp = [math.inf for _ in range(n+1)]
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(nums[i], n+1):
                dp[j] = min(dp[j], dp[j - nums[i]]+1)
        
        return dp[-1]
