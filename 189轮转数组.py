class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #方法一 使用队列 34/38
        while k > 0:
            queue = []
            while len(nums) != 1:
                queue.append(nums.pop(0))
            while queue:
                nums.append(queue.pop(0))
            k -= 1
        return

        #方法二 巧用旋转法
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        nums.reverse()
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
