class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token not in lst:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    num = num1 + num2
                elif token == "-":
                    num = num2 - num1
                elif token == "*":
                    num = num1 * num2
                else:
                    num = int(num2/num1)
                stack.append(num)
        return stack[-1]
