#动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        nums1 = nums[:-1]
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums1[i-2])
        
        ans = dp[-1]

        nums2 = nums[1:]
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums2[i-2])
        
        return max(ans, dp[-1])
