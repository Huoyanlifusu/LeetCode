class Solution(object):
    def missingTwo(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) + 2
        cur = n * (n+1) // 2 - sum(nums)
        tot, t = cur, cur // 2
        cur = t * (t+1) // 2 - sum([x for x in nums if x <= t])
        return [cur, tot-cur]