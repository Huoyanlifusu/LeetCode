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

    
    #简洁双指针
    class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)
        def reverse(lst, start, end):
            left, right = start, end-1
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            return
        
        for i in range(0, len(lst), 2*k):
            if i+k <= len(lst):
                reverse(lst, i, i+k)
            else:
                reverse(lst, i, len(lst))
            
        return "".join(lst)
