expression = input("输入表达式")
# 回溯查找的思想，对每一个符号，都认为他的优先级是最高的
# 然后查找他左右式子的所有运算结果的可能性即可
l = []
i = 0
while i < len(expression):
    if expression[i].isdigit():
        x = 0
        while i < len(expression) and expression[i].isdigit():
            x = x * 10 + int(expression[i])
            i += 1
        l.append(x)
    else:
        l.append(expression[i])
        i += 1


def dfs(l):
    if len(l) == 1:
        return [l[0]]

    vals = []
    for i in range(1, len(l), 2):
        left_vals = dfs(l[:i])
        right_vals = dfs(l[i+1:])
        for left_val in left_vals:
            for right_val in right_vals:
                if l[i] == "+":
                    vals.append(left_val+right_val)
                elif l[i] == "-":
                    vals.append(left_val-right_val)
                elif l[i] == "*":
                    vals.append(left_val * right_val)
    return vals

print(dfs(l))