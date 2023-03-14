#构造队列 算法时长超过97%的用户
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        sign = x / abs(x)
        x *= sign

        queue = []
        c = 0
        val = 0
        while abs(x) >= 10:
            queue.append(x%10)
            x /= 10
            c += 1

        queue.append(x%10)
        for num in queue:
            val += num * pow(10, c)
            c -= 1
        
        val *= sign

        if val > pow(2, 31) -1 or val < -1 * pow(2, 31):
            return 0

        return val
