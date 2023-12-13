# 动态规划
flowerbed = list(map(int, input("输入数组").split()))

n = int(input("输入n"))

flowerbed = [0] + flowerbed + [0]
l = len(flowerbed)
dp = [0] * l
# dp数组表示从第0个花坛到第i个花坛最多可以种植多少花
for i in range(1, l-1):
    # 递推公式
    # 正常情况下，如果这个花坛旁边以及本身都没有花，那么可以种植花朵，
    # 递推公式就是前一个和前两个+1中取最大
    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
        dp[i] = max(dp[i-2]+1, dp[i-1])
    # 如果两边或本身种上了花，那么无法种花了，就跟着上一个的最大值
    else:
        dp[i] = dp[i-1]

print(dp[-2]>=n)