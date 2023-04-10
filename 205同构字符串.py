class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for index, char in enumerate(s):
            if char not in map1:
                map1[char] = t[index]
            elif map1[char] != t[index]:
                return False
        
        for index, char in enumerate(t):
            if char not in map2:
                map2[char] = s[index]
            elif map2[char] != s[index]:
                return False

        return True
