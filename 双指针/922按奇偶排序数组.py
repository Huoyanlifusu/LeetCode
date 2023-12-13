# 暴力法 O(n^2) 超时 57/61
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

# 构造新数组 O(n)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        even = 0
        odd = 1
        for num in nums:
            if num % 2 == 0:
                result[even] = num
                even += 2
            else:
                result[odd] = num
                odd += 2
        return result

# 原地修改法 
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[odd] % 2:
                    odd += 2
                nums[i], nums[odd] = nums[odd], nums[i]
        return nums
