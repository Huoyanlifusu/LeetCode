#bfs 85/89

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        steps = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        g = len(grid)
        end = [g-1, g-1]
        def updatestep(cur, step):
            return [cur[0]+step[0], cur[1]+step[1]]

        queue = collections.deque()
        queue.append([0,0])

        visited = set()
        for i in range(g):
            for j in range(g):
                if grid[i][j] == 1:
                    visited.add(str(i)+str(j))

        result = 1
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur == end:
                    return result
                if str(cur[0])+str(cur[1]) in visited:
                    continue
                visited.add(str(cur[0])+str(cur[1]))
                for step in steps:
                    newstep = updatestep(cur, step)
                    if newstep[0] >= 0 and newstep[0] < g and newstep[1] >= 0 and newstep[1] < g and str(newstep[0])+str(newstep[1]) not in visited:
                        queue.append(newstep)
            result += 1

        return -1
