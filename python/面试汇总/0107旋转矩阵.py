class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-i-1], matrix[n-1-i][n-1-j]
        
        return