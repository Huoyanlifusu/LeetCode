nums = list(map(int, input("输入数组").split(" ")))
l = len(nums)
for i in range(l):
    m, n = 0, 1
    while n < l - i and m < l - i:
        val = nums[m]%2
        if val == 1:
            nums[m], nums[n] = nums[n], nums[m]
        m += 1
        n += 1

print(nums)