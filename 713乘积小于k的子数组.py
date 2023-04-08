class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        chengji = 1
        left = 0
        
        for right, num in enumerate(nums):
            chengji *= num
            while chengji >= k:
                chengji /= nums[left]
                left += 1
            ans += right - left + 1
        
        return ans
