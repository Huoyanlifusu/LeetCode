class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        dic = {}
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                dic[num] = dic[num] + 1 if num in dic else 1
        lst = []
        for num in dic.keys():
            for i in range(dic[num]):
                lst.append(num)
        return lst
