# https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue:

    def __init__(self):
        self.stack = []
        self.healperStack = []

    def push(self, x: int) -> None:
        stacklen = len(self.stack)
        if stacklen > 0:
            for i in range(stacklen):
                self.healperStack.append(self.stack.pop())
            self.stack.append(x)
            for i in range(stacklen):
                self.stack.append(self.healperStack.pop())
        else:
            self.stack.append(x)
    def pop(self) -> int:
         return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0