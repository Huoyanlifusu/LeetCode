class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            if nums[fast] == 0:
                fast += 1
            else:
                fast += 1
                slow += 1
            if fast == len(nums):
                while slow < len(nums):
                    nums[slow] = 0
                    slow += 1
