class Solution(object):
    def findClosedNumbers(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i, j = num+1, num-1
        cnt = bin(num)[2:].count("1")
        cnt_max = bin(2147483647)[2:].count("1")
        if cnt == cnt_max:
            return [-1, -1]
        while bin(i)[2:].count("1") != cnt:
            i += 1
        while bin(j)[2:].count("1") != cnt:
            j -= 1
        return [i, j]