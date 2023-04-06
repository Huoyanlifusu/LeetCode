#43/56用例
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        use = [0 for _ in range(len(nums))]
        arr = []
        result = []
        def backsearch(nums, startIndex, used):
            if startIndex == len(nums): return
            for i in range(startIndex, len(nums)):
                if (i > 0 and nums[i-1] == nums[i] and used[i-1] == 0) or (arr and nums[i] < arr[-1]):
                    continue
                if (i > 1 and nums[i-2] == nums[i-1] == nums[i]) or (i < len(nums) - 2 and nums[i] == nums[i+1] == nums[i+2]):
                    continue
                arr.append(nums[i])
                if len(arr) > 1:
                    result.append(list(arr))
                used[i] = 1
                backsearch(nums, i+1, used)
                used[i] = 0
                arr.pop()

        backsearch(nums, 0, use)
        return result
