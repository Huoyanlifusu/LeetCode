class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        array = [[]]

        def backsearch(nums, startindex):
            for i in range(startindex, len(nums)):
                path.append(nums[i])
                array.append(path.copy())
                backsearch(nums, i+1)
                path.pop()
        
        backsearch(nums, 0)
        return array
