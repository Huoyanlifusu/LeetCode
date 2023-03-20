class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        
        quotient = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** quotient % 1000000007
        elif remainder == 1:
            return 3 ** (quotient-1) * 4 % 1000000007
        else:
            return 3 ** quotient * 2 % 1000000007
