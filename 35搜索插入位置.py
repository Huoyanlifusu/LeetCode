class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if target>nums[mid]:
                left = mid + 1
            elif target<nums[mid]:
                right = mid - 1
            else:
                return mid
        return max(left,right)
