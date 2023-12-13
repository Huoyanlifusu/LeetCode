nums = list(map(int, input("请输入").split(" ")))

# 动态规划
# n = len(nums)
# dp = [float("inf")] * n
# dp[0] = 0
# for i in range(1, n):
#     for j in range(i):
#         if nums[j] + j >= i:
#             dp[i] = min(dp[i], dp[j]+1)
# print(dp[-1])

# 维护一个当前的最远距离 和 一个下次的最远距离
# 当到达当前最远距离时，更新到下一次的最远距离，此时step+1 这是一种贪心的思想
# 然后判断是否到达终点，是则跳出循环，否则继续遍历

end, max_pos = 0, 0
steps = 0
for i in range(len(nums)-1):
    max_pos = max(max_pos, nums[i]+i)
    if i == end:
        end = max_pos
        steps += 1
