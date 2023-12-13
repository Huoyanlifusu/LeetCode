import threading
def say():
    lock.acquire()
    print(1)
    lock.release()
    print(2)
    lock.acquire()
    print(3)
    lock.release()
    print(4)


if __name__ == "__main__":
    t = threading.Thread(target=say)
    lock = threading.Lock()

    t.start()