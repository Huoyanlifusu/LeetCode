class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        return len(set(dic.values())) == 1
