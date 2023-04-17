class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        for char in num1:
            n1 = n1 * 10 + int(char)
        
        n2 = 0
        for char in num2:
            n2 = n2 * 10 + int(char)
        
        n = n1 + n2
        ans = ""
        while n > 0:
            ans = str(n%10) + ans
            n //= 10
        return ans if ans else "0"
