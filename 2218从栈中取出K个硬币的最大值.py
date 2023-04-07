#回溯算法 时间复杂度过大
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        path = []
        def popstacktop(stack):
            stack2 = []
            while stack:
                stack2.append(stack.pop())
            num = stack2.pop()
            while stack2:
                stack.append(stack2.pop())
            return num
        
        def insertstacktop(stack, num):
            stack2 = []
            while stack:
                stack2.append(stack.pop())
            stack2.append(num)
            while stack2:
                stack.append(stack2.pop())

        def backsearch(piles, startIndex, k, max_price):
            if k == 0: return max(max_price, sum(path))

            for i in range(len(piles)):
                if not piles[i]: continue
                num = popstacktop(piles[i])
                path.append(num)
                max_price = backsearch(piles, i, k-1, max_price)
                insertstacktop(piles[i], num)
                path.pop()
