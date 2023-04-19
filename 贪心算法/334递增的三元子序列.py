class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lst = [nums[0]]
        n = len(nums)
        for index in range(1, n):
            if len(lst) >= 3:
                break
            cur = nums[index]
            if lst[-1] < cur:
                lst.append(cur)
            else:
                if cur < lst[0] and index < n-2:
                    lst[0] = cur 
                elif cur > lst[0] and cur < lst[1] and index < n-1:
                    lst[1] = cur
        
        return True if len(lst) > 2 else False
