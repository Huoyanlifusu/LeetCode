#贪心
#先饼干在胃口
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
#先胃口再饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        index = len(s) - 1
        for i in range(len(g)-1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                index -= 1
                result += 1
        return result
