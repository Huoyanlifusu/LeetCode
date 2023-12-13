class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = [0] * 4
        r1, c1, r2, c2 = [0] * 4
        max_sum = matrix[0][0] # 全局最大和
        for i in range(m): # 起始行
            total = [0] * n
            for j in range(i, m): # 结束行
                cur_max = 0
                for k in range(n):
                    # 其实如果不需要统计坐标的只是寻找最大和的话
                    """
                    根连续的子序列的最大和的题写法是一样的
                    cur_max = max(cur_max, cur_max + total[k])
                    max_sum = max(cur_max, max_sum)
                    
                    只不过这里要求统计左上角和右下角的坐标，所以要使用if else 拆开然后记录行号和列号
                    """
                    total[k] += matrix[j][k]
                    if cur_max > 0: # cur_max + total[k] > cur_max 加了比不加更大
                        cur_max += total[k] # 那就加上去
                    else: # cur_max + total[k] <= cur_max 加了变得更小了
                        cur_max = total[k] # 那就不用加了
                        r1 = i # 更新行起点
                        c1 = k # 更新列起点
                    if cur_max > max_sum: # 如果当前和比全局最大和大了
                        r2, c2 = j, k # 更新一下行终点和列终点
                        max_sum = cur_max # 更新当前和为全局最大和
                        ans = r1, c1, r2, c2 # 更新结果
        return ans