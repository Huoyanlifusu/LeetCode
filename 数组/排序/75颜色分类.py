#快速排序

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, start, end):
            i = start - 1
            pivot = end
            for left in range(start, end):
                if nums[left] < nums[pivot]:
                    i += 1
                    if i != left:
                        nums[i], nums[left] = nums[left], nums[i]
            i += 1
            nums[i], nums[pivot] = nums[pivot], nums[i]
            return i
        
        def quicksort(nums, left, right):
            if left > right: return

            pi = partition(nums, left, right)
            quicksort(nums, left, pi-1)
            quicksort(nums, pi+1, right)

        quicksort(nums, 0, len(nums)-1)
