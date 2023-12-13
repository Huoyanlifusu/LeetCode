class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = dict()

        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
        
        maxNum = minLen = 0
        for cnt, left, right in mp.values():
            if cnt > maxNum:
                maxNum = cnt
                minLen = right - left + 1
            elif cnt == maxNum:
                minLen = min(minLen, right-left+1)

        return minLen