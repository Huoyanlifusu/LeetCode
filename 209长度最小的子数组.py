#滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        s = 0
        left = 0
        ans = len(nums)+1
        for right, num in enumerate(nums):
            s += num
            while s >= target:
                ans = min(right-left+1, ans)
                s -= nums[left]
                left += 1
        return ans
