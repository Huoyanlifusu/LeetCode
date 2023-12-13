# 给定一个 R行 C列 的整数网格 Grid，找出一条包含节点最多的路，
# 使得路上的每个节点的值依次递减，每个节点可以朝上下左右行走 注意不能沿着对角线方向行走 或者走到边界外

R, C = map(int, input("请输入行列数").split(" "))

grid = []
for i in range(R):
    grid.append(tuple(map(int, input("请输入第%i行数据" %(i,)).split(" "))))

max_node = 0

f = [[-1]*C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def valid(i, j, val):
    if i < 0 or j < 0 or i >= R or j >= C:
        return False
    if grid[i][j] < val:
        return True
    return False

def dfs(i, j):
    if f[i][j] != -1:
        return f[i][j]
    f[i][j] = 1
    t = 0
    val = grid[i][j]
    for n in range(4):
        x, y = i + dx[n], j + dy[n]
        if valid(x, y, val):
            t = max(t, dfs(x, y))
    f[i][j] += t
    return f[i][j]

for i in range(R):
    for j in range(C):
        max_node = max(max_node, dfs(i, j))

print(max_node)