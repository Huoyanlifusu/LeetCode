#本质上还是完全背包
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [0 for _ in range(amount+1)]
        for j in range(1, amount+1):
            dp[j] = math.inf

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j-coins[i]]+1, dp[j])
        
        if dp[-1] == math.inf: return -1
        return dp[-1]
