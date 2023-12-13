class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(2, n+2):
            dp[i] = max(nums[i-2]+dp[i-2], dp[i-1])
        return dp[n+1]