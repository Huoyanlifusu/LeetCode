class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        col = len(obstacleGrid[0])
        row = len(obstacleGrid)
        map = [[0 for i in range(col)] for i in range(row)]
        for i in range(0, row):
            if obstacleGrid[i][0] == 1:
                break
            map[i][0] = 1
        for j in range(0, col):
            if obstacleGrid[0][j] == 1:
                break
            map[0][j] = 1
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    map[i][j] = map[i-1][j] + map[i][j-1]
        return map[-1][-1]
