class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
          return []
        elif shorter == longer:
          return [shorter*k]
        res = [shorter*k]
        for i in range(k):
          res.append(res[-1]+longer-shorter)
        return res