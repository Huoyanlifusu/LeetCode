class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        for i in range(1,target//2 + 1):
            res = [i]
            while sum(res) < target:
                res.append(res[-1]+1)
            if sum(res) == target:
                ans.append(res)
        return ans
