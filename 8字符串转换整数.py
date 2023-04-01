class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+',s.lstrip())),pow(2,31)-1), pow(-2,31))
