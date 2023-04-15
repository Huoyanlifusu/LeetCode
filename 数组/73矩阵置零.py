class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        points = []
        for i in range(m):
            for j in range(n):
                if [i,j] in points:
                    continue
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            points.append([i,k])
                            matrix[i][k] = 0
                    for k in range(m):
                        if matrix[k][j] != 0:
                            points.append([k,j])
                            matrix[k][j] = 0
