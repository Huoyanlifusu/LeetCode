# 模拟整个流程即可
import collections
tasks = input("输入任务序列").split()

n = int(input("输入冷却时间"))

dic = collections.defaultdict(int)
for task in tasks:
    dic[task] += 1

waited = [0] * 26
work_queue = []
time = 0
while True:
    if not dic:
        break

    i = 0
    while i < len(work_queue):
        waited[work_queue[i]] -= 1
        if waited[work_queue[i]] == 0:
            work_queue.pop(i)
        else:
            i += 1

    time += 1
    if all(waited[ord(key)-ord('A')] > 0 for key in dic.keys()):
        continue

    items = sorted(dic.items(), key=lambda x:-x[1])

    for item in items:
        key = item[0]
        index = ord(key)-ord('A')
        if not waited[index]:
            waited[index] = n+1
            work_queue.append(index)
            dic[key] -= 1
            if dic[key] == 0:
                del dic[key]
            break

print(time)