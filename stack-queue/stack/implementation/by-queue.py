# https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        lenOfQueue = len(self.queue)
        if lenOfQueue != 1:
            for i in range(lenOfQueue - 1):
                self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue