#排序+双指针
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)

        best = 10**7

        for i in range(l):
            j, k = i+1, l-1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == target:
                    return target
                if value > target:
                    if abs(value - target) < abs(best - target):
                        best = value
                    k -= 1
                    continue
                if value < target:
                    if abs(value - target) < abs(best - target):
                        best = value
                    j += 1
                    continue
        
        return best
