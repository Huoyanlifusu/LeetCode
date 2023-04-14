class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        t, b = 0, m
        l, r = 0, n
        count = 0
        nums = []
        while count < m * n:
            for i in range(l, r):
                nums.append(matrix[t][i])
                count += 1
            t += 1
            for i in range(t, b):
                nums.append(matrix[i][r-1])
                count += 1
            r -= 1
            for i in range(r-1, l-1, -1):
                nums.append(matrix[b-1][i])
                count += 1
            b -= 1
            for i in range(b-1, t-1, -1):
                nums.append(matrix[i][l])
                count += 1
            l += 1
        return nums[0:m*n]
