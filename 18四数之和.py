#剪枝双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-3):
            if nums[i] > target and nums[i] > 0 and target > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] > target and target > 0 and nums[i] + nums[j] > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    value = nums[i] + nums[j] + nums[left] + nums[right]
                    if value == target:
                        tmp = [nums[i], nums[j], nums[left], nums[right]]
                        if tmp not in result:
                            result.append(tmp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif value > target:
                        right -= 1
                    else:
                        left += 1
        
        return result
