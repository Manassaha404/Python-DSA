# Online Stock Span
# https://leetcode.com/problems/online-stock-span/description/

# Time Complexity  : Amortized O(1) per next() call — across N calls, each price is pushed and popped at most once (overall O(N) time for N calls)
# Space Complexity : O(N) — where N is the total number of calls to next(), storing elements in the monotonic stack
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        prevG = -1
        stack = self.stack
        while stack and stack[-1][1] <= price:
            stack.pop()
        if self.stack:
            prevG = stack[-1][0]
        stack.append([self.index, price])
        days = self.index - prevG
        return days  