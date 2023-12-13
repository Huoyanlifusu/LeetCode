class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0] * (n+1)
        for i in range(1, n+1):
            f[i] = f[i-1] + 1
            for j in range(i):
                if sentence[j:i] in dictionary:
                    f[i] = min(f[i], f[j])
        return f[n]