# 排序 + 双指针
class Solution(object):
    def findSwapValues(self, array1, array2):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: List[int]
        """
        array1.sort()
        array2.sort()
        a, b = sum(array1), sum(array2)
        diff = a - b
        i, j, m, n = 0, 0, len(array1), len(array2)
        res = []
        while i < m and j < n:
            if diff == 2 * (array1[i] - array2[j]):
                res = [array1[i], array2[j]]
                break
            elif diff > 2 * (array1[i] - array2[j]):
                i += 1
            else:
                j += 1
        return res