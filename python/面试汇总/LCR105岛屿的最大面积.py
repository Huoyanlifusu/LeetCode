class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited = [[0] * n for _ in range(m)]

        def valid(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if visited[x][y] == 0 and grid[x][y] == 1:
                return True
            return False

        def bfs(x, y, area):
            q = [(x, y)]
            while q:
                x, y = q.pop(0)
                for i in range(4):
                    nx, ny = x+dx[i],y+dy[i]
                    if valid(nx, ny):
                        visited[nx][ny] = 1
                        area += 1
                        q.append((nx, ny))
            return area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    res = max(res, bfs(i, j, 1))
                    
        return res