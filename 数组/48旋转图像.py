class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            res = []
            for j in range(i+1, n-i):
                res.append(matrix[i][j])
            for j in range(i+1, n-i):
                res.append(matrix[j][n-1-i])
                matrix[j][n-1-i] = res.pop(0)
            for j in range(n-i-2, i-1, -1):
                res.append(matrix[n-1-i][j])
                matrix[n-1-i][j] = res.pop(0)
            for j in range(n-i-2, i-1, -1):
                res.append(matrix[j][i])
                matrix[j][i] = res.pop(0)
            for j in range(i+1, n-i):
                matrix[i][j] = res.pop(0)
