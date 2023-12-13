class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
            
        rows, cols = [False] * m, [False] * n


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = 0 if rows[i] or cols[j] else matrix[i][j]
        