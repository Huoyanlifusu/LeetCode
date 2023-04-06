#回溯算法 16/20用例 算法复杂度过大
import sys

categoty = int(input())
def backsearch(lst, startindex, weight, ans):
    if startindex == len(lst): return
    for i in range(startindex, len(lst)):
        if i > 0 and lst[i] == lst[i-1] and i != startindex: continue
        weight += lst[i]
        if weight not in ans: ans.append(weight)
        backsearch(lst, i + 1, weight, ans)
        weight -= lst[i]
    return ans

weights = input().split(" ")
nums = input().split(" ")
lst = []
for index, weight in enumerate(weights):
    while int(nums[index]) > 0:
        nums[index] = str(chr(ord(nums[index]) - 1))
        lst.append(int(weight))
ans = backsearch(lst, 0, 0, [0])
print(len(ans))
