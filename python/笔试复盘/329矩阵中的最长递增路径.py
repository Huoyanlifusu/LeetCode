class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        f = [[-1] * n for _ in range(m)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def isValid(x, y, cmp_val):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if matrix[x][y] > cmp_val:
                return True
            return False
        
        def dfs(x, y):
            if f[x][y] != -1:
                return f[x][y]
            
            f[x][y] = 1
            t = 0
            for i in range(4):
                if isValid(x+dx[i], y+dy[i], matrix[x][y]):
                    t = max(t, dfs(x+dx[i], y+dy[i]))
            
            f[x][y] += t
            return f[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res