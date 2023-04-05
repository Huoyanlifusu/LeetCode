from math import pi
import sys
s = input().split(" ")
lst = []
for word in s:
    for char in word:
        if char.islower() or char.isupper():
            lst.append(char)

# def quicksort(lst, start, end):
#     if start >= end: return
#     p = partition(lst, start, end)
#     quicksort(lst, start, p-1)
#     quicksort(lst, p+1, end)

# def partition(lst, start, end):
#     i = start - 1
#     pivot = end
#     for j in range(start, end):
#         if ord(lst[j].upper()) <= ord(lst[pivot].upper()):
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     lst[i+1], lst[pivot] = lst[pivot], lst[i+1]
#     return (i+1)

lst = sorted(lst, key = str.upper)
for word in s:
    tmp = ""
    for char in word:
        if char.islower() or char.isupper():
            tmp += lst.pop(0)
        else:
            tmp += char
    print(tmp, end = " ")
