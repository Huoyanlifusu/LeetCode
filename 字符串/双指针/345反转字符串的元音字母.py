class Solution:
    def reverseVowels(self, s: str) -> str:
        ref = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            while s[left] not in ref:
                left += 1
                if left >= right:
                    return "".join(s)
            while s[right] not in ref:
                right -= 1
                if left >= right:
                    return "".join(s)
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)
