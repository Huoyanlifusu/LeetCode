# 模拟 + 贪心的思路
target = int(input("目标距离"))
startfuel = int(input("初始的油量"))
stations = list(map(int, input("输入加油站信息").split()))

n = len(stations)
while n >= 2:
    n -= 2
    stations.append((stations.pop(0), stations.pop(0)))

print(stations)

def solution(target, startfuel, stations):
    fuels = []
    fuel_time = 0
    cur_end = startfuel
    stations.append((target, 0))
    for station in stations:
        while cur_end < station[0]:
            if not fuels:
                return -1
            mv = max(fuels)
            cur_end += mv
            fuels.remove(mv)
            fuel_time += 1
        if cur_end >= station[0]:
            fuels.append(station[1])
    if cur_end < target:
        return -1
    return fuel_time

if startfuel > target:
    print(0)
else:
    res = solution(target, startfuel, stations)
    print(res)
