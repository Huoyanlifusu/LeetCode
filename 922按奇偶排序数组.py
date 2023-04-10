class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        used = []
        for index, num in enumerate(nums):
            if index % 2 == 0 and num % 2 != 0:
                for swapindex in range(index+1, len(nums)):
                    if nums[swapindex] % 2 == 0:
                        nums[index], nums[swapindex] = nums[swapindex], nums[index]
            elif index % 2 != 0 and num % 2 == 0:
                for swapindex in range(index+1, len(nums)):
                    if nums[swapindex] % 2 == 1:
                        nums[index], nums[swapindex] = nums[swapindex], nums[index]
        return nums
