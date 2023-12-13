# 有向图问题 先考虑能不能广搜 再考虑深搜
class Solution(object):
    def findWhetherExistsPath(self, n, graph, start, target):
        """
        :type n: int
        :type graph: List[List[int]]
        :type start: int
        :type target: int
        :rtype: bool
        """
        g = [[] for _ in range(n)]
        visited = set()
        for route in graph:
            g[route[0]].append(route[1])
        
        q = [start]
        while q:
            x = q.pop(0)
            for v in g[x]:
                if v == target:
                    return True
                if v not in visited:
                    q.append(v)
                    visited.add(v)
        
        return False