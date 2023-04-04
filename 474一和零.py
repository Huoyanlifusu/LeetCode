#0-1背包
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            x, y = 0, 0
            for char in s:
                if char == "0":
                    x+=1
                else:
                    y+=1
            for i in range(m, x-1, -1):
                for j in range(n, y-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y] + 1)
        
        return dp[m][n]
