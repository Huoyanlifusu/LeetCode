#模拟
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        step = m+n
        res = []
        for i in range(1, step):
            if i % 2:
                if i <= m:
                    for j in range(min(i, n)):
                        res.append(mat[i-1-j][j])
                else:
                    for j in range(min(m+n-i,m)):
                        res.append(mat[m-1-j][n-(m+n-i-j)])
            else:
                if i <= n:
                    for j in range(min(i, m)):
                        res.append(mat[j][i-j-1])
                else:
                    for j in range(min(m+n-i, n)):
                        res.append(mat[m-(m+n-i-j)][n-1-j])
        return res
