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

#bfs 也可行 python 记录父节点时内存爆表
import sys
m, n = map(int, input().split(" "))
nums = []
for line in sys.stdin:
    nums.append(list(map(int, line.split(" "))))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
end = [m-1, n-1]
queue = [[0,0]]
path = []
while queue:
    start = queue.pop(0)
    for i in range(4):
        newstart = [start[0]+dx[i], start[1]+dy[i]]
        if newstart[0] >= m or newstart[0] < 0 or newstart[1] >= n or newstart[1] < 0: continue
        if nums[newstart[0]][newstart[1]] == 1: continue
        nums[newstart[0]][newstart[1]] = 1
        queue.append(newstart)

    if start == end:
        path.append(start)

print(path)
