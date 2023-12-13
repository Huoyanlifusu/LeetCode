import threading
import time


def say1():
    with lock1:
        time.sleep(0.1)
        print("a")
        with lock2:
            print("b")
        print("c")

def say2():
    with lock2:
        time.sleep(0.1)
        print("e")
        with lock1:
            print("f")
        print("g")

if __name__ == "__main__":
    # 死锁的情况2
    lock1 = threading.RLock()
    lock2 = threading.RLock()
    t1 = threading.Thread(target=say1)
    t2 = threading.Thread(target=say2)
    t1.start()
    t2.start()