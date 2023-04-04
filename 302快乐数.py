class Solution:
    def isHappy(self, n: int) -> bool:
        lst = [n]
        while True:
            n = lst[-1]
            while n % 10 == 0 or n == 1:
                if n == 1:
                    return True
                n //= 10
            n = lst[-1]
            tmp = []
            while n >= 1:
                tmp.append(n%10)
                n //= 10
            for num in tmp:
                n += num * num
            if n in lst:
                return False
            lst.append(n)
