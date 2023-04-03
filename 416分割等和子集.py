class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNUm = sum(nums)
        if sumNUm % 2 == 1:
            return False
        target = sumNUm//2
        if max(nums) > target:
            return False
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target, 0, -1):
                if j >= nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        if target == dp[target]:
            return True
        else:
            return False
