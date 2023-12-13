class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
          if i < nums[i]:
            i = nums[i]
          elif i == nums[i]:
            return i
          else:
            i += 1
        return -1