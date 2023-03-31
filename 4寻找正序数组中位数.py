class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pointer1, pointer2 = 0, 0
        nums = []
        while pointer1 < len(nums1) or pointer2 < len(nums2):
            if pointer1 == len(nums1):
                nums.append(nums2[pointer2])
                pointer2 += 1
                continue
            if pointer2 == len(nums2):
                nums.append(nums1[pointer1])
                pointer1 += 1
                continue
            num1 = nums1[pointer1]
            num2 = nums2[pointer2]
            if num1 <= num2:
                nums.append(num1)
                pointer1 += 1
            else:
                nums.append(num2)
                pointer2 += 1
        l = len(nums)
        if l % 2 == 1:
            return float(nums[l//2])
        else:
            return float(nums[l//2] + nums[l//2-1])/2.0
