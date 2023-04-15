#0-1背包问题 石头分成两堆重量最为近似的相互碰撞
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumNum = sum(stones)
        target = sumNum//2
        dp = [0] * (target+1)

        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sumNum - dp[target] * 2
