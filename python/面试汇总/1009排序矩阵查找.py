class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] > target:
                return False
            if matrix[i][-1] < target:
                continue
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False