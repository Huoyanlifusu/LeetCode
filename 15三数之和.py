#双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0: return []
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0: return result
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums)-1
            while left < right:
                value = [nums[i], nums[left], nums[right]]
                if sum(value) == 0:
                    if value not in result: 
                        result.append(value)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif sum(value) > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
