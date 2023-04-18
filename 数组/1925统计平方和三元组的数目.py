class Solution:
    def countTriples(self, n: int) -> int:
        dic = {}
        for i in range(1,n+1):
            dic[i*i] = 1
        res = 0
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                if i*i + j*j in dic:
                    res += 2
        return res
