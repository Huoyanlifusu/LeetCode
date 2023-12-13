# 一个项目包括n个活动，分别为A1、A2、A3…An；活动之间有依赖关系，如[Ax, Ay]表示必须先完成Ay才能完成Ax
#（即Ax活动依赖Ay活动）。现在请你排一个计划，列出各活动之间的先后顺序（如有多个顺序返回其中一种即可）。

# 示例1:
# 输入: 4 [[0, 1],[1, 3],[1, 2]]——表示总共四个活动，
# 活动之间依赖关系：0号活动依赖活动1、1号活动依赖活动3、1号活动同时依赖活动2
# 输出: [3 2 1 0]——表示先进行活动3、再进行活动2、然后进行活动1、最后进行活动0


# 请候选人实现：
# 1、	实现函数：输入是总活动个数、以及活动间依赖关系，输出一种活动安排计划
# ——注：输入确保有效（且无循环依赖）

# def solution(n, acs):
#     mp = [[] for _ in range(n)]
#     mp_res = [[] for _ in range(n)]
#     d = [0 for _ in range(n)]
#     visited = [0] * n

#     res = []
#     for ac in acs:
#         [x, y] = ac
#         mp[x].append(y)
#         d[y] += 1

#     def dfs(x):
#         for y in mp[x]:
#             if visited[y] == 0:
#                 if d[y] > 1:
#                     mp_res[y].append(x)
#                     d[y] -= 1
#                 elif d[y] == 1:
#                     dfs(y)
#                     res.append(y)
#                     for k in mp_res[y]:
#                         res.append(k)
#                     visited[y] = 1
#                     d[y] -= 1
    
#     i = 0
#     while i < n:
#         if d[i] == 0 and visited[i] == 0:
#             dfs(i)
#             res.append(i)
#         i += 1

#     return res

# print(solution(4, [[0, 1],[1, 3],[1, 2]]))

import collections

def solution(n, prerequisites):
    edges = collections.defaultdict(list)
    indeg = [0] * n

    result = list()

    for info in prerequisites:
        edges[info[1]].append(info[0])
        indeg[info[0]] += 1
    
    q = collections.deque([u for u in range(n) if indeg[u] == 0])

    while q:
        u = q.popleft()
        result.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(result) != n:
        result = list()
    return result