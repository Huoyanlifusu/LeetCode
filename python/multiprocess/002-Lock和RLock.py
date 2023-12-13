import threading
import time

lock = threading.Lock()

def say1():
    lock.acquire()
    print("我喜欢说话1")
    time.sleep(0.5)
    lock.release()

def say2():
    lock.acquire()
    print("我喜欢说话2")
    time.sleep(0.5)
    lock.release()
    

if __name__ == "__main__":
    t1 = threading.Thread(target=say1)
    t2 = threading.Thread(target=say2)

    t1.start()
    t2.start()