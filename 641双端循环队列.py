class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.tmpqueue = []

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.size:
            while self.queue:
                self.tmpqueue.append(self.queue.pop(0))
            self.queue.append(value)
            while self.tmpqueue:
                self.queue.append(self.tmpqueue.pop(0))
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.queue):
            return False
        return True

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False
