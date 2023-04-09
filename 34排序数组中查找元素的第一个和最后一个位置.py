class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = [-1,-1]
        for index, num in enumerate(nums):
            if res[0] == -1 and num == target:
                res[0] = index
            if (index < n - 1 and num == target and nums[index+1] != target) or (index == n-1 and num == target):
                res[1] = index
        return res
