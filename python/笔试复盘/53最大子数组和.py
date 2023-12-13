nums = list(map(int, input("输入数组").split()))

n = len(nums)
dp = [0] * n
dp[0] = nums[0] #dp数组 表示 从第0个元素到第i个元素里的最大子数组和

for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i]) #递推公式 
    #说明了两种情况
    #第一种情况是使用前面的子数组加上当前元素值
    #第二种情况是不使用前面的子数组，以当前元素为头重新开辟一个子数组
    
print(max(dp))