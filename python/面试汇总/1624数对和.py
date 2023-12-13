class Solution(object):
    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        i, j = 0, len(nums) - 1
        res = []

        while i < j and len(nums) > 1:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target: i += 1
            else: j -= 1
        
        return res