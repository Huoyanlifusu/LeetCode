n = 10
dp = [0] * (n+1)
for i in range(2, n+1):
    for j in range(i):
        dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
print(dp[n])