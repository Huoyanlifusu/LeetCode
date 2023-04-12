#贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        cover = nums[0]
        i = 1
        while i <= cover:
            cover = max(cover, nums[i]+i)
            if cover >= n-1:
                return True
            i += 1
        return False
