import threading
from concurrent.futures import ThreadPoolExecutor
import time
import multiprocessing

def say(num):
    print("执行", num)
    time.sleep(2)

# 进程池里的add_done_callback由主进程执行
# 线程池里的add_done_callback由子线程执行

def done(fur):
    print(threading.current_thread().getName())
    time.sleep(1)
    print(fur.result())
    time.sleep(1)
    

if __name__ == "__main__":
    pool = ThreadPoolExecutor(4)

    for i in range(10):
        fur = pool.submit(say, i)
        fur.add_done_callback(done)

    
    print(threading.current_thread().getName())
    pool.shutdown(True)
