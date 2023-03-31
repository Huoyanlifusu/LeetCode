class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            dpn = 0
            for j in range(1, i):
                dpn = max(dpn, j*(i-j), j*dp[i-j])
            dp[i] = dpn
        return dp[n]
