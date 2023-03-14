#滑动窗口
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        left = 0

        l = len(s)

        Set = set()

        max_len = 0
        cur_len = 0

        for i in range(l):
            cur_len += 1
            while s[i] in Set:
                Set.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            Set.add(s[i])
        return max_len
        
