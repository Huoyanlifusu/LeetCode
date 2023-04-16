class CustomStack:
    def __init__(self, maxSize: int):
        self.stack1 = []
        self.stack2 = []
        self.max_len = maxSize

    def push(self, x: int) -> None:
        if len(self.stack1) < self.max_len:
            self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()

    def increment(self, k: int, val: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        while self.stack2:
            if k:
                self.stack1.append(self.stack2.pop()+val)
                k -= 1
            else:
                self.stack1.append(self.stack2.pop())
