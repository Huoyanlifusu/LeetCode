class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]
        p, q = 1, 1
        for i in range(1, n):
            p *= nums[i-1]
            res.append(p)
        for i in range(n-2, -1, -1):
            q *= nums[i+1]
            res[i] *= q
        return res
