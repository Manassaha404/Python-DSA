# Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/ 

def largestRectangleArea(heights: list[int]) -> int:
    # Approach 1: Finding Prev Smaller and Next Smaller via separate passes (commented out)
    # Time Complexity  : O(N) — 3 passes (prevSmaller: O(N), nextSmaller: O(N), area calculation: O(N))
    # Space Complexity : O(N) — auxiliary prevS, nextS arrays of size N and monotonic stack of size up to N
    # def prevSmaller(arr):
    #     n = len(arr)
    #     result = [-1] * n
    #     stack = []
    #     for i in range(n):
    #         while stack and arr[stack[-1]] >= arr[i]:
    #             stack.pop()
    #         if stack:
    #             result[i] = stack[-1]
    #         stack.append(i)
    #     return result
    # def nextSmaller(arr):
    #     n = len(arr)
    #     result = [n] * n
    #     stack = []
    #     for i in range(n - 1, -1, -1):
    #         while stack and arr[stack[-1]] >= arr[i]:
    #             stack.pop()
    #         if stack:
    #             result[i] = stack[-1]
    #         stack.append(i)
    #     return result
    # prevS = prevSmaller(heights)
    # nextS = nextSmaller(heights)
    # largest = -1
    # for i in range(len(heights)):
    #     prevSI = prevS[i]
    #     nextSI = nextS[i]
    #     width = nextSI - prevSI - 1
    #     largest = max(largest, heights[i] * width)
    # return largest

    # Approach 2: Precomputed Next Smaller + Running Prev Smaller using Stack (commented out)
    # Time Complexity  : O(N) — 2 passes (nextSmaller: O(N) + running pass: O(N))
    # Space Complexity : O(N) — auxiliary nextS array of size N and monotonic stack of size up to N
    # def nextSmaller(arr):
    #     n = len(arr)
    #     result = [n] * n
    #     stack = []
    #     for i in range(n - 1, -1, -1):
    #         while stack and arr[stack[-1]] >= arr[i]:
    #             stack.pop()
    #         if stack:
    #             result[i] = stack[-1]
    #         stack.append(i)
    #     return result
    # stack = []
    # nextS = nextSmaller(heights)
    # largest = -1
    # for i in range(len(heights)):
    #     while stack and heights[stack[-1]] > heights[i]:
    #         stack.pop()
    #     prevS = -1
    #     if stack:
    #         prevS = stack[-1]
    #     nextSI = nextS[i]
    #     width = nextSI - prevS - 1
    #     largest = max(largest, heights[i] * width)
    #     stack.append(i)
    # return largest

    # Approach 3: Single Pass Monotonic Stack (active)
    # Time Complexity  : O(N) — single pass; each bar index is pushed and popped from the stack at most once
    # Space Complexity : O(N) — monotonic stack storing at most N indices (worst case: strictly increasing heights)
    n = len(heights)
    stack = []
    largest = -1
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            idx = stack.pop()
            prevS = -1
            nextS = i
            if stack:
                prevS = stack[-1]
            width = nextS - prevS - 1
            largest = max(largest, heights[idx] * width)
        stack.append(i)
    while stack:
        idx = stack.pop()
        prevS = -1
        nextS = n
        if stack:
            prevS = stack[-1]
        width = nextS - prevS - 1
        largest = max(largest, heights[idx] * width)
    return largest