# 给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
# 示例：
# 输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# 输出：3，即数值对(11, 8)
# 提示：
# 1 <= a.length, b.length <= 100000
# -2147483648 <= a[i], b[i] <= 2147483647
# 正确结果在区间 [0, 2147483647] 内

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

i, j = 0, 0
m, n = len(l1), len(l2)

res = float("inf")

while i < m and j < n:
    res = min(res, abs(l1[i]-l2[j]))
    if l1[i] == l2[j]:
        break
    elif l1[i] < l2[j]:
        i += 1
    else:
        j += 1

print(res)