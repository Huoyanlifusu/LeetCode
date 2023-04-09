class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0 for _ in range(k*2)]
        for i, num in enumerate(dp):
            if i % 2 == 0:
                dp[i] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[0] = max(dp[0], -prices[i])
            for j in range(1, len(dp)):
                if j % 2 == 1:
                    dp[j] = max(dp[j], dp[j-1]+prices[i])
                else:
                    dp[j] = max(dp[j], dp[j-1]-prices[i])
        return dp[-1]
