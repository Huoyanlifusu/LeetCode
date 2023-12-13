class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, num = len(s), 0
        st = []
        preSign = "+"
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == n-1 or s[i] in "+-*/":
                if preSign == "+":
                    st.append(num)
                elif preSign == "-":
                    st.append(-num)
                elif preSign == "*":
                    st.append(st.pop()*num)
                elif preSign == "/":
                    val = st.pop()
                    if val < 0: st.append(abs(val)/num*-1)
                    else: st.append(val/num)
                preSign = s[i]
                num = 0
        return sum(st)