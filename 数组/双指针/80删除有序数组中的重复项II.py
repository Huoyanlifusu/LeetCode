class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = 0, 0
        count = 0
        res = 0
        while fast < n:
            origin = fast
            tmp = nums[fast]
            while fast < n and nums[fast] == tmp:
                fast += 1
            l = fast - origin
            if l >= 2:
                nums[slow] = tmp
                slow += 1
                nums[slow] = tmp
                slow += 1
                res += 2
            else:
                nums[slow] = tmp
                slow += 1
                res += 1
                
        return res
