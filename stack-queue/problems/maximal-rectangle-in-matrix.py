# Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/description/

# Time Complexity  : O(R * C) — where R is the number of rows and C is the number of columns.
#                    O(R * C) to compute column-wise consecutive 1 heights, and R * O(C) for largestRectangleArea across all rows.
# Space Complexity : O(C) — auxiliary space for the monotonic stack of size at most C (the matrix is updated in-place)
def maximalRectangle(matrix: list[list[str]]) -> int:
    for col in range(len(matrix[0])):
        prefixSum = 0
        for row in range(len(matrix)):
            if int(matrix[row][col]) != 0:
                prefixSum += 1
                matrix[row][col] = prefixSum
            else:
                prefixSum = 0
                matrix[row][col] = 0
    largest = 0

    def largestRectangleArea(heights: list[int]) -> int:
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

    for row in matrix:
        largest = max(largest, largestRectangleArea(row))
    return largest