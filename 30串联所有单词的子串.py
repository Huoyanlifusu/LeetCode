#滑动窗口
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        n = len(s)
        words_num = len(words)
        words = Counter(words)
        index = []
        for i in range(0, word_len):
            res = []

            left = i
            right = i
            cur_num = 0
            cur_cnt = Counter()
            while right + word_len <= n:
                word = s[right:right+word_len]
                right += word_len
                if word not in words:
                    left = right
                    cur_cnt.clear()
                    cur_num = 0
                else:
                    cur_cnt[word] += 1
                    cur_num += 1
                    while cur_cnt[word] > words[word]:
                        left_word = s[left:left+word_len]
                        left += word_len
                        cur_cnt[left_word] -= 1
                        cur_num -= 1
                    if cur_cnt == words:
                        index.append(left)
        return index
#暴力算法 简化版本
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        m = len(words[0])
        k = len(s)
        refdic = collections.Counter(words)
        if k < m*n:
            return []
        result = []
        for i in range(k-m*n+1):
            tmps = s[i:i+n*m]
            dic = {}
            for j in range(n):
                tmp = tmps[j*m:j*m+m]
                if tmp not in dic:
                    dic[tmp] = 1
                else:
                    dic[tmp] += 1
            if dic == refdic:
                result.append(i)
        
        return result
