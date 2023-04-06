class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for index, char in enumerate(s):
            if cnt[char] == 1:
                return index
        return -1
