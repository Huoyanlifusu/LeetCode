word1 = input("输入字符串1")
word2 = input("输入字符串2")

m = len(word1)
n = len(word2)

dp = [[0]*(n+1) for _ in range(m+1)]
dp[0] = [i for i in range(n+1)]

for i in range(1, m+1):
    dp[i][0] = i
    for j in range(1, n+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

print(dp[m][n])