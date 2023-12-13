class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        def nextDay(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in xrange(8)]

        m = len(cells)
        states = {}
        i = 0
        while n > 0:
            state = tuple(cells)
            if state in states:
                n = n % (states[state] - n)
            states[state] = n
            
            if n >= 1:
                n -= 1
                cells = nextDay(cells)
        
        return cells