#您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。 9/10
#二分查找
import sys

cube = float(input())

start = cube
target = start * start * start
target = round(target, 1)
while target != cube:
    if target > cube:
        if cube >= 0:
            start -= start/2.0
        else:
            start += start/2.0
    else:
        if cube >= 0:
            start += start/2.0
        else:
            start -= start/2.0
    target = start*start*start
    target = round(target, 1)

print(round(start, 1))
