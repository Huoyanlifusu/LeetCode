# 创建型
import threading
class Singleton(object):
    _instance_lock = threading.Lock()
    def __new__(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self) -> None:
        pass

obj1 = Singleton()
obj2 = Singleton()

print(obj1, obj2)