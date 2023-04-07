#回溯算法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backsearch(nums, startindex, used, path, result):
            if len(path) == len(nums): 
                result.append(list(path))
                return
            for i in range(len(nums)):
                if used[i] == 1: continue
                path.append(nums[i])
                used[i] = 1
                backsearch(nums, 0, used, path, result)
                path.pop()
                used[i] = 0
            return result
        
        return backsearch(nums, 0, [0 for _ in range(len(nums))], [], [])
