class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [[True for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

        f = [math.inf for i in range(n)]
        
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        f[i] = min(f[j]+1, f[i])
        return f[n-1]
        
