#哈希
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {}
        for char in magazine:
            if char not in dic1:
                dic1[char] = 1
            else:
                dic1[char] += 1
        
        for char in ransomNote:
            if char not in dic1 or dic1[char] <= 0:
                return False
            else:
                dic1[char] -= 1
        
        return True
