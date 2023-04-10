class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        result = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
            result = max(dp[i]) if max(dp[i]) > result else result
        
        return result
