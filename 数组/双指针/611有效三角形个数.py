class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(len(nums)-1, -1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    res += r-l
                    r -= 1
        return res
