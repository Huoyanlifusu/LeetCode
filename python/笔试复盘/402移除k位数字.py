stack = []

num = input("输入num")
k = int(input("输入k"))

for digit in num:
    while stack and k and stack[-1] > digit:
        stack.pop()
        k -= 1
    stack.append(digit)

s = "".join(stack).lstrip('0') or '0'
print(s)