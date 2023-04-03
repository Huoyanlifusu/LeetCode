#贪心
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        index = 0
        for i in range(len(g)):
            while index < len(s):
                if s[index] >= g[i]:
                    result += 1
                    index += 1
                    break
                index += 1
        return result
