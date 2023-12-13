# 贪心算法
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic = {}
        res = 0
        for num in answers:
            dic[num] = dic.get(num, 0) + 1
        # k 是多少个兔子跟自己颜色一样
        # v 是说了k的兔子个数
        for k, v in dic.items():
            if k+1 >= v:
                res += k+1
            else:
                while v > 0:
                    v -= k+1
                    res += k+1
        return res