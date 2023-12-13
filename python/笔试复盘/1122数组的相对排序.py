# 思路 快排
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(arr2):
            dic[num] = i
        

        def partition(arr, left, right):
            pivot = left
            i = left + 1
            for j in range(left+1, right):
                if arr[pivot] in dic and arr[j] in dic and dic[arr[pivot]] >= dic[arr[j]]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                elif arr[pivot] not in dic and arr[j] in dic:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                elif arr[pivot] not in dic and arr[j] not in dic and arr[pivot] >= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
            return i-1


        def quicksort(arr, left, right):
            if left >= right:
                return
            pi = partition(arr, left, right)
            quicksort(arr, left, pi)
            quicksort(arr, pi+1, right)
        

        quicksort(arr1, 0, len(arr1))
        return arr1