#动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1]-prices[i])
            dp[1] = max(dp[1], dp[0]+prices[i])
        return dp[1]
#贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i]-prices[i-1], 0)
        return result
