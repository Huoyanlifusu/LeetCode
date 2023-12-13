class Solution(object):
    def minTime(self, time, m):
        """
        :type time: List[int]
        :type m: int
        :rtype: int
        """
        l, r = 0, sum(time)

        def check(t, cost, mdy):
            cdy, cdt, mcost = 1, 0, cost[0]

            for i in cost[1:]:
                if cdt + min(i, mcost) <= t:
                    cdt += min(i, mcost)
                    mcost = max(i, mcost)
                else:
                    cdy += 1
                    cdt = 0
                    mcost = i
            return cdy <= mdy

        while l < r:
            mid = (l+r)//2
            if check(mid, time, m):
                r = mid
            else:
                l = mid + 1
        
        return l