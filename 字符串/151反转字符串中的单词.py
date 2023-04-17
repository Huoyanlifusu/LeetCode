class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.strip().split()
        ans = ""
        for word in lst:
            ans = " " + word + ans
        return ans.lstrip()
