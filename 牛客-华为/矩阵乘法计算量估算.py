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
stack = []
for char in rule:
    if char == "(":
        continue
    elif char != ")":
        stack.append(char)
    else:
        k = 2
        tmp = []
        while k > 0:
            k -= 1
            s = stack.pop()
            if s == "ref":
                tmp.append(mats.pop())
            else:
                tmp.append(mats[ord(s) - ord('A')])
        res = compute(tmp[1], tmp[0])
        mats.append(res[0:2])
        result += res[2]
        stack.append("ref")

print(result)
