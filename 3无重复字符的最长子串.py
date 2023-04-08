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
        
#简化版本
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        tmp = ""
        left = 0

        for right, char in enumerate(s):
            while char in tmp:
                tmp = tmp[1:]
                left += 1
            tmp += char
            ans = max(ans, right-left+1)
        
        return ans
