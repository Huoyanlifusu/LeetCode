# 模拟碰撞的思想
# 只有一种情况左边的小行星会和右边的小行星相撞
# 就是左边的小行星向右，右边的小行星向左
asteroids = list(map(int, input("输入小行星").split()))

i = 0
while i < len(asteroids):
    if i < len(asteroids)-1 and asteroids[i] > 0 and asteroids[i+1] < 0:
        if asteroids[i] == -asteroids[i+1]:
            asteroids = asteroids[:i] + asteroids[i+2:]
            if i > 0:
                i -= 1
        elif asteroids[i] > -asteroids[i+1]:
            asteroids = asteroids[:i+1] + asteroids[i+2:]
        else:
            asteroids = asteroids[:i] + asteroids[i+1:]
            if i > 0:
                i -= 1
    else:
        i += 1

print(asteroids)