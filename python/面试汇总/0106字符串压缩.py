class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        i, j, n = 0, 0, len(S)
        while i < n:
            ch = S[i]
            m = 1
            j = i+1
            while j < n and S[j] == ch:
                j += 1
                m += 1
            res += ch + str(m)
            if len(res) >= n:
                break
            i = j
        
        return res if len(res) < n else S