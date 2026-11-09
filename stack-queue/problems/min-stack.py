# Min Stack
# https://leetcode.com/problems/min-stack/description/

# Time Complexity: O(1) for all operations (push, pop, top, getMin)
# Space Complexity: O(N) where N is the number of elements in the stack
class MinStack:
    # formula = 2val - min < val ;;; 2val - min = newVal;;; newMin = val

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(value)
            self.min = value
        elif value < self.min:
            newVal = 2 * value - self.min
            self.min = value
            self.stack.append(newVal)
        else:
            self.stack.append(value)

    def pop(self) -> None:
        popVal = self.stack.pop()
        if popVal < self.min:
            newMin = 2 * self.min - popVal
            popEl = self.min
            self.min = newMin
            return popEl
        else:
            return popVal

    def top(self) -> int:
        topEl = self.stack[len(self.stack) - 1]
        if topEl < self.min:
            return self.min
        else:
            return topEl

    def getMin(self) -> int:
        return self.min 