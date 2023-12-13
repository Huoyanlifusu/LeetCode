# Python 解决哈希冲突用的是开放地址法

class HashClass(object):
    def __hash__(self) -> int:
        return 42

e = HashClass()
f = HashClass()

dic = {e: "a", f:"b"}
print(e)
print(f)