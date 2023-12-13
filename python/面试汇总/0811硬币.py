# 动态规划
class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        coins = [1, 5, 10, 25]
        for coin in coins:
            for x in range(coin, n+1):
                dp[x] += dp[x-coin]
        return dp[n] % 1000000007