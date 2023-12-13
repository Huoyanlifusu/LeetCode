n = int(input("输入节点个数"))

dp = [0] * (n+2)
dp[0] = 1
dp[1] = 1
dp[2] = 2

# 说白了，n较大的情况可以从n较小的情况进行递推
# 如果n为0，即没有二叉搜索树，此时只有一种情况
# 如果n为1，即一个节点，此时也只有一种情况
# 如果n为2，有两个节点，比如1和2，那么可能是 1（根节点）-2 或 1-2（根节点）两种情况
# 因此，dp数组表示当有n个节点的时候，能构建的二叉搜索树个数

def solution(n):
    if n <= 2:
        return dp[n]
    for i in range(3, n+1):
        res = 0
        # 分别考虑每个节点当根节点的情况，就会有i个不同的根节点
        for j in range(i):
            left_cnt = j
            right_cnt = i-j-1
            res += dp[left_cnt] * dp[right_cnt]
            # 递推公式 分别考虑当前根节点下 左右节点可能有多少种摆放方式
            # 然后把左孩子乘上右孩子的个数 得到的就是当前根节点的总构建分类个数
        dp[i] = res
    return dp[n]

print(solution(n))


