#回溯算法 
#关键在理解树层去重，树枝不去重
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        use = [0 for _ in range(len(nums))]
        arr = []
        result = [[]]
        def backsearch(nums, startindex, used):
            if startindex == len(nums): return
            for i in range(startindex, len(nums)):
                if i > 0 and nums[i-1] == nums[i] and used[i-1] == 0:
                    continue
                used[i] = 1
                arr.append(nums[i])
                result.append(list(arr))
                backsearch(nums, i + 1, used)
                used[i] = 0
                arr.pop()
        backsearch(nums, 0, use)
        return result
