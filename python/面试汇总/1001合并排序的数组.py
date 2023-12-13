class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 or j >= 0:
            if i == -1:
                A[k] = B[j]
                j -= 1
            elif j == -1:
                A[k] = A[i]
                i -= 1
            elif A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A