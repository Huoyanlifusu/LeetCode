#回溯超时 48/70

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1 for _ in range(len(nums))]
        def backsearch(nums, i, cache):
            if i < 0: return 0
            if cache[i] != -1: return cache[i]
            res = max(backsearch(nums, i-1, cache), backsearch(nums, i-2, cache)+nums[i])
            return res
        
        return backsearch(nums, len(nums)-1, cache)
