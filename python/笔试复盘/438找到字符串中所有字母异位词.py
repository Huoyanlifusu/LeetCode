class Solution(object):
    # 滑动窗口的思想 + 数组顺序表替代哈希表
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m, res = len(s), len(p), []
        if n < m: return res

        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(m):
            s_cnt[ord(s[i])-ord('a')] += 1
            p_cnt[ord(p[i])-ord('a')] += 1
        
        if s_cnt == p_cnt:
            res.append(0)

        for i in range(m, n):
            s_cnt[ord(s[i])-ord('a')] += 1
            s_cnt[ord(s[i-m])-ord('a')] -= 1
            if s_cnt == p_cnt:
                res.append(i-m+1)
        return res