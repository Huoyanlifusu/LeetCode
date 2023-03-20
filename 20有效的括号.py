class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2==1: return False

        stack = []

        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        
        for char in s:
            if char in pairs:
                if not stack or pairs[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        
        return not stack
