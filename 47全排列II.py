class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backsearch(nums, startindex, used, path, result):
            if len(path) == len(nums):
                result.append(list(path))
                return

            uset = set()
            for i in range(startindex, len(nums)):
                if nums[i] in uset or used[i] == 1:
                    continue
                uset.add(nums[i])
                path.append(nums[i])
                used[i] = 1
                backsearch(nums, 0, used, path, result)
                path.pop()
                used[i] = 0
            
            return result

        return backsearch(nums, 0, [0 for _ in range(len(nums))], [], [])
