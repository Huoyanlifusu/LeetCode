#16/20 回溯超时
import sys

num = int(input())
nums = list(map(int, input().strip().split(" ")))

# def quicksort(nums, start, end):
#     if start > end: return
#     pivot = partition(nums, start, end)
#     quicksort(nums, start, pivot-1)
#     quicksort(nums, pivot+1, end)

# def partition(nums, start, end):
#     pivot = nums[end]
#     i = start - 1
#     for j in range(start, end):
#         if nums[j] < pivot:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#     i += 1
#     nums[i], nums[end] = nums[end], nums[i]
#     return i
    
# quicksort(lst, 0, len(lst)-1)
result = 0
def backsearch(nums, startindex, path):
    global result
    if startindex == len(nums): 
        return
    for i in range(startindex, len(nums)):
        if path and nums[i] <= path[-1]: continue
        path.append(nums[i])
        result = max(result, len(path))
        backsearch(nums, i+1, path)
        path.pop()

backsearch(nums, 0, [])
print(result)
