# 用两个栈实现

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        st1, st2 = [], []
        for ch in num1:
            st1.append(int(ch))
        for ch in num2:
            st2.append(int(ch))
        jinwei = 0
        res = ""
        while st1 or st2 or jinwei:
            n1 = st1.pop() if st1 else 0
            n2 = st2.pop() if st2 else 0

            cur = n1 + n2 + jinwei
            jinwei = cur // 10
            cur = cur % 10

            res = str(cur) + res

        return res
