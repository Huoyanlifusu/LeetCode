class Solution:
    def reverseWords(self, s: str) -> str:
        chars = s.split()
        ans = []
        while chars:
            char = list(chars.pop(0))
            char.reverse()
            ans.append("".join(char))
        return " ".join(ans)
