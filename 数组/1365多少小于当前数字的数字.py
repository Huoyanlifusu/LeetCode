#哈希
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = collections.Counter(nums)
        ans = []
        for num in nums:
            tmp = 0
            for refnum in dic:
                if refnum < num:
                    tmp += dic[refnum]
            ans.append(tmp)
        return ans
