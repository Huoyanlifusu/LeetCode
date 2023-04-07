#数学归纳法
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]

#动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1, 2]
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for j in range(1, n+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        
        return dp[-1]
