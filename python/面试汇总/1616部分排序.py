class Solution(object):
    def subSort(self, array):
        """
        :type array: List[int]
        :rtype: List[int]
        """
        array_1 = array[:]
        array_1.sort()

        if array_1 == array:
            return [-1, -1]
        n = len(array)
        for i in range(n):
            if array[i] != array_1[i]:
                break
        
        for j in range(n-1, -1, -1):
            if array[j] != array_1[j]:
                break
        return [i, j]