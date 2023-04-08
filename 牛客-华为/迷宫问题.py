#dfs 回溯暴搜
import sys
import math
m, n = map(int, input().split(" "))
nums = []
for line in sys.stdin:
    nums.append(list(map(int, line.split(" "))))

def backsearch(m, n, nums, start, end, path, result):
    if start == end:
        result = path.copy()
        return result
    steps = [(0,1), (1,0), (-1,0), (0,-1)]
    for step in steps:
        nstep = (start[0] + step[0], start[1] + step[1])
        if nstep[0] < 0 or nstep[0] >= m or nstep[1] < 0 or nstep[1] >= n:
            continue
        if nums[nstep[0]][nstep[1]] == 1:
            continue
        path.append(nstep)
        nums[nstep[0]][nstep[1]] = 1
        result = backsearch(m, n, nums, nstep, end, path, result)
        nums[nstep[0]][nstep[1]] = 0
        path.pop()
    return result

res = backsearch(m, n, nums, (0,0), (m-1, n-1), [(0,0)], ())
for step in res:
    print("("+str(step[0])+","+str(step[1])+")")

#bfs 也可行
