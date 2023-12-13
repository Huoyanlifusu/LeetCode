import threading
from concurrent.futures import ThreadPoolExecutor
from collections.abc import Hashable
import collections
import time
from functools import reduce

def sing():
    for _ in range(10):
        print("sing")

def dance(num):
    for _ in range(num):
        print("dance")

class Singleton:
    instance = None
    lock = threading.RLock()

    def __init__(self, name) -> None:
        self.name = name
    
    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


if __name__ == "__main__":
    ThreadPoolExecutor()
    # s = {1:1}
    # print(isinstance((1), Hashable))

    # a = reduce(lambda x, y: x+y, [1, 2, 3, 4])
    # m = map(lambda x: x<0, [-1, -5, 3, 2])
    # print(a)
    # print(m)
    # obj1 = Singleton("laowang")
    # print(id(obj1))

    # obj2 = Singleton("laozhang")
    # print(id(obj2))

    # 查看线程
    # print(threading.enumerate())
    # print(type(threading.Thread))

    # 线程池
    # pool = ThreadPoolExecutor(10)
    # pool.submit(sing())

    # print(dir(object))
    
    # 创建多任务
    # t3 = threading.Thread(target=dance, args=(5,))
    # t3.start()
    # t1 = threading.Thread(target=sing)
    # t2 = threading.Thread(target=dance)
    # t1.start()
    # t2.start()