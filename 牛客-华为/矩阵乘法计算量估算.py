# 19/20
import sys
n = int(input())
mats = []
i = 0
while i < n:
    mats.append(list(map(int, input().split())))
    i += 1

rule = input()

def compute(mat1, mat2):
    newrow = mat1[0]
    newcol = mat2[1]
    return [newrow, newcol, mat1[0]*mat2[1]*mat1[1]]

result = 0
ref = []
stack = []
for char in rule:
    if char == "(":
        continue
    elif char != ")":
        stack.append(char)
    else:
        if not ref:
            mat2 = mats[ord(stack.pop()) - ord('A')]
            mat1 = mats[ord(stack.pop()) - ord('A')]
            tmp = compute(mat1, mat2)
            ref = tmp[0:2]
            result += tmp[2]
            stack.append("ref")
            continue
        k = 2
        tmp = []
        while k > 0:
            k -= 1
            s = stack.pop()
            if s == "ref":
                tmp.append(ref)
            else:
                tmp.append(mats[ord(s) - ord('A')])
        res = compute(tmp[1], tmp[0])
        ref = res[0:2]
        result += res[2]
        stack.append("ref")

print(result)
