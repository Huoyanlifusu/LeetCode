
s = input("请输入括号字符串")

stack = [] #括号 暂存
indexs = [] #括号索引 暂存
valid = []

for i, ch in enumerate(s):
    if ch == "(":
        stack.append("(")
        indexs.append(i)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
            valid.append(i)
            valid.append(indexs.pop())

valid.sort()

i = 0
res = 0
ans = 0
while i < max(valid):
    if i in valid and i+1 in valid:
        res += 2
        i += 2
        ans = max(ans, res)
    else:
        res = 0
        i += 1

print(ans)