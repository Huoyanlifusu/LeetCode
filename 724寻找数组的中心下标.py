class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumnum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if sumnum - leftsum - nums[i] == leftsum:
                return i
            leftsum += nums[i]
        return -1
