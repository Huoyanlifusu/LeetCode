# 动态规划 所有的递增子序列类似题目都是这个格式
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j]+1)
        return max(f)