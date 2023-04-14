class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        m = len(grid)
        n = len(grid[0])
        for i in range(n):
            step = [0, i]
            while step[0] < m:
                if grid[step[0]][step[1]] == 1:
                    step[1] += 1
                    if step[1] > n-1 or grid[step[0]][step[1]] == -1:
                        break
                    step[0] += 1
                else:
                    step[1] -= 1
                    if step[1] < 0 or grid[step[0]][step[1]] == 1:
                        break
                    step[0] += 1
            
            if step[0] != m:
                answer.append(-1)
            else:
                answer.append(step[1])
        
        return answer
