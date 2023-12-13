n = int(input())

graph = [[] for _ in range(n)]
f = [[0,0] for _ in range(n)]
d = [0 for _ in range(n)]


for _ in range(n):
    line = input().split()
    root = int(line[0][0])
    cnt = int(line[0][3])

    for i in range(1, 1+cnt):
        leaf = int(line[i])
        graph[root].append(leaf)
        d[leaf] += 1

root = 0
while d[root] > 0:
    root += 1

def dfs(u):
    f[u][1] = 1
    f[u][0] = 0
    for x in graph[u]:
        dfs(x)
        f[u][1] += min(f[x][0], f[x][1])
        f[u][0] += f[x][1]

dfs(root)
res = min(f[root][0], f[root][1])
print(res)
