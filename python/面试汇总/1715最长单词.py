class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(word, ref):
            if word == "":
                return True
            res = False
            for i in range(1, len(word)+1):
                if word[:i] in words and word[:i] != ref:
                    res = res or dfs(word[i:], ref)
            return res
        ans = ""
        for word in words:
            if dfs(word, word):
                if len(word) > len(ans): ans = word
                elif len(word) == len(ans) and word < ans: ans = word
        return ans
