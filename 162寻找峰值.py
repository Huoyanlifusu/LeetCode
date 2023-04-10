class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        nums.insert(0, -math.inf)
        nums.append(-math.inf)
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                return mid-1
