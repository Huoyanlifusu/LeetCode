class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0]*n]*m
        for i in range(m):
            map[i][0] = 1
        for j in range(n):
            map[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                map[i][j] = map[i-1][j] + map[i][j-1]
        return map[-1][-1]
