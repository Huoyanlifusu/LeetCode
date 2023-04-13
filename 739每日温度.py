# 暴力法 两层for循环 32/48用例
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = []
        for index, num in enumerate(temperatures):
            for j in range(index+1, len(temperatures)):
                if temperatures[j] > num:
                    lst.append(j-index)
                    break
                if j == len(temperatures)-1:
                    lst.append(0)
        lst.append(0)
        return lst

# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0 for _ in range(n)]
        stack.append(0)
        for i in range(1, n):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    j = stack.pop()
                    result[j] = i-j
                stack.append(i)
        return result
