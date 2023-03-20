class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)
        left, right = 0, 0
        max_count = 0
        res_str = ""
        while right <= len(s) - 1:
            if s[right] not in res_str:
                res_str = s[left:right+1]
                max_count = max(max_count, len(res_str))
                right += 1
                continue
            
            while s[right] in res_str:
                left += 1
                res_str = res_str[1:]
            
        return max_count
