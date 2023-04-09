#二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0.0
        right = float(x)
        while left <= right:
            mid = left + (right-left)/2.0
            if int(mid * mid) > x:
                right = mid
            elif int(mid * mid) < x:
                left = mid
            else:
                return int(mid)
