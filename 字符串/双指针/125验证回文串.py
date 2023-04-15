class Solution:
    def isPalindrome(self, s: str) -> bool:
        ref = "0123456789"
        tmp = ""
        for char in s:
            if char.isupper():
                tmp += char.lower()
            elif char.islower() or char in ref:
                tmp += char
        
        left = 0
        right = len(tmp)-1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        return True
