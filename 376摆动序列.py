#贪心算法
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        prediff = 0
        curdiff = 0
        count = 1
        for i in range(len(nums) - 1):
            curdiff = nums[i+1] - nums[i]
            if (prediff <= 0 and curdiff > 0) or (prediff >= 0 and curdiff < 0):
                count += 1
                prediff = curdiff
        return count
