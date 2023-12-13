# 双指针
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, n = 0, 0, len(s)
        dic = dict()
        res = 0
        while i < n and j < n:
            if s[i] not in dic:
                dic[s[i]] = 1
                i += 1
                res = max(res, i-j)
                continue
            while s[i] in dic:
                del dic[s[j]]
                j += 1

        return res