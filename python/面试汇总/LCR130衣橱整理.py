class Solution(object):
    def wardrobeFinishing(self, m, n, cnt):
        """
        :type m: int
        :type n: int
        :type cnt: int
        :rtype: int
        """
        vis = [[0] * (n+1) for _ in range(m+1)]
        vis[0][1], vis[1][0] = 1, 1
        def qiuhe(i, j):
          return sum(list(map(int, str(i)+str(j))))
          
        res = 0
        for i in range(1, m+1):
          for j in range(1, n+1):
            if qiuhe(i-1, j-1) <= cnt and (vis[i-1][j] == 1 or vis[i][j-1] == 1):
                res += 1
                vis[i][j] = 1
        return res