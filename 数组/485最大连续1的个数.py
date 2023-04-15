class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        while right < len(nums):
            if nums[right] != 1:
                right += 1
                left += 1
                continue
            else:
                while right < len(nums) and nums[right] == 1:
                    right += 1
                result = right - left if right - left > result else result
                left = right
        return result
