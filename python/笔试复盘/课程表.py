class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        mp = [{} for _ in range(n+1)]
        for u, v, t in times:
            mp[u][v] = t

        r = [-1 for _ in range(n+1)]
        r[k] = 0

        q = [(k, 0)]
        while q:
            cur, t = q.pop(0)
            for u, v in mp[cur].items():
                art = t + v
                if r[u] == -1 or r[u] > art:
                    r[u] = art
                    q.append((u, art))
        
        minT = -1
        for i in range(1, n+1):
            if r[i] == -1:
                return -1
            minT = max(minT, r[i])
        
        return minT