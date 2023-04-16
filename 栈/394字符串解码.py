class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        multi = 0
        for c in s:
            if c == "[":
                stack.append([multi, res])
                multi, res = 0, ""
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + res * cur_multi
            elif "9" >= c >= "0":
                multi = multi*10 + int(c)
            else:
                res += c
        return res
