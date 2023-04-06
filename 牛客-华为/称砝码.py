#回溯算法 内存超限制
import sys

categoty = int(input())
def backsearch(lst, startindex, weight, ans):
    if startindex == len(lst): return
    for i in range(startindex, len(lst)):
        if i > 0 and lst[i] == lst[i-1] and i != startindex: continue
        weight += lst[i]
        ans.append(weight)
        backsearch(lst, i + 1, weight, ans)
        weight -= lst[i]
    return ans

weights = []
for line in sys.stdin:
    w, n = map(int, line.split(" "))
    while n > 0:
        weights.append(w)


ans = backsearch(weights, 0, 0, [])
print(ans)
