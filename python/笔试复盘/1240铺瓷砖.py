n = int(input("输入行数")) # 瓷砖行数
m = int(input("输入列数")) # 瓷砖列数

grids = [[False] * m for _ in range(n)]
max_cnt = [max(m, n)]

def isAvaliable(x, y, k):
    for i in range(k):
        for j in range(k):
            if grids[x+i][y+j] == True:
                return False
    return True

def fillUp(x, y, k, val):
    for i in range(k):
        for j in range(k):
            grids[x+i][y+j] = val

def dfs(x, y, cnt, max_cnt):
    if cnt >= max_cnt[0]:
        return

    if x >= n:
        max_cnt[0] = cnt
        return
    
    if y >= m:
        dfs(x+1, 0, cnt, max_cnt)
        return
    
    if grids[x][y] == True:
        dfs(x, y+1, cnt, max_cnt)
        return
    
    k = min(n-x, m-y)

    while k >= 1 and not isAvaliable(x, y, k):
        k -= 1
    
    while k >= 1:
        fillUp(x, y, k, True)
        dfs(x, y+k, cnt+1, max_cnt)
        fillUp(x, y, k, False)
        k -= 1

dfs(0, 0, 0, max_cnt)
print(max_cnt[0])