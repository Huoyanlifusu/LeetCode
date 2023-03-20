class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if pushed == popped: return True
        size = len(pushed)

        stack = []
        c = 0
        for index in range(size):
            stack.append(pushed[index])

            while stack:
                if stack[-1] != popped[0]:
                    break
                else:
                    stack.pop()
                    popped.pop(0)

        if stack == []:
            return True
        return False
