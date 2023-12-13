import copy

a = [11, 22]
b = [33, 44]

c = [a, b]

d = copy.deepcopy(c)
e = copy.copy(c)

a.append(55)

print(c)
print(d)
print(e)