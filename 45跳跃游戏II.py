#贪心算法
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        cover = 0
        Next = 0
        step = 0
        for i in range(n):
            Next = max(Next, nums[i]+i)
            if i == cover:
                if cover < n-1:
                    step += 1
                    cover = Next
                    if cover >= n-1:
                        break
        
        return step
