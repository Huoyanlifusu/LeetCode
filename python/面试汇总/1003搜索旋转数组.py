# 二分查找，重点在于分析边界问题
class Solution(object):
    def search(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            if arr[left] == target:
                return left
            mid = left + (right - left) // 2
            if arr[mid] == target:
                right = mid
            elif arr[0] < arr[mid]:
                if arr[0] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[0] > arr[mid]:
                if arr[mid] < target <= arr[n-1]:
                    left = mid + 1
                else:
                    right = mid -1
            else:
                left = left + 1
        return -1