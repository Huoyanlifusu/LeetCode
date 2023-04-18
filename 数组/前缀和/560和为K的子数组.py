class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = {0:1}
        presum = 0
        res = 0
        for i in range(n):
            presum += nums[i]
            if presum - k in dic:
                res += dic[presum-k]
            dic[presum] = dic.get(presum, 0) + 1
        return res
