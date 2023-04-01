class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        stack = []
        lst = []
        newStr = ""

        while s:
            if len(s) > k:
                for i in range(k):
                   stack.append(s[0])
                   s = s[1:]
                while stack:
                    newStr += stack.pop()
            else:
                newStr += s[::-1]
                s = ""
                break
            if len(s) > k:
                for i in range(k):
                    lst.append(s[0])
                    s = s[1:]
                while lst:
                    newStr += lst.pop(0)
            else:
                newStr += s
                s = ""
                break

        return newStr
