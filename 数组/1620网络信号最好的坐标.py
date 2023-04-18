import math
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        n = len(towers)
        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0
        for i in range(n):
            max_x = max(max_x, towers[i][0]+radius)
            max_y = max(max_y, towers[i][1]+radius)
        
        def calculateSignal(i, j):
            res = 0
            for tower in towers:
                d = (tower[0]-i)*(tower[0]-i) + (tower[1]-j)*(tower[1]-j)
                if d > radius*radius:
                    continue
                res += int(tower[2]/(1+math.sqrt(d)))
            return res
        index = [0,0]
        maxsignal = 0
        for i in range(min_x, max_x+1):
            for j in range(min_y, max_y+1):
                tmp = calculateSignal(i, j)
                if tmp > maxsignal:
                    index = [i, j]
                    maxsignal = tmp
        
        return index
