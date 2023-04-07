#树枝剪枝 数层去重 回溯查找组合
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr = []
        result = []
        def backsearch(nums, startIndex):
            if len(arr) > 1: result.append(list(arr))
            if startIndex == len(nums): return
            uset = set()
            for i in range(startIndex, len(nums)):
                if (nums[i] in uset) or (len(arr) > 0 and nums[i] < arr[-1]):
                    continue
                arr.append(nums[i])
                uset.add(nums[i])
                backsearch(nums, i+1)
                arr.pop()

        backsearch(nums, 0)
        return result
