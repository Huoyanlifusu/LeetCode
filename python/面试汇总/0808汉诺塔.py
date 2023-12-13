class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        n = len(A)
        if n == 1:
            C.append(A.pop(0))
            return
        B = A[1:]
        C.append(A[0])
        A = []
        self.hanota(B,A,C)