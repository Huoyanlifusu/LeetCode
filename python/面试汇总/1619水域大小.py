class Solution(object):
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        dx, dy = [0,0,-1,1,-1,1,-1,1], [1,-1,0,0,-1,1,1,-1]
        m, n = len(land), len(land[0])
        visited = [[0] * n for _ in range(m)]
        def valid(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if visited[x][y] == 0 and land[x][y] == 0:
                visited[x][y] = 1
                return True
            return False
        
        def bfs(i, j, area):
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if valid(nx, ny):
                        area += 1
                        q.append((nx, ny))
            return area
        
        res = []
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and land[i][j] == 0:
                    visited[i][j] = 1
                    res.append(bfs(i, j, 1))
        res.sort()
        return res