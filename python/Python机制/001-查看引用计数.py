# 查看引用计数
import sys

class A:
    def __init__(self, name):
        self.name = name

a = A("laowangg")
print(sys.getrefcount(a))