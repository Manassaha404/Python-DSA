# zig zag grid traversal 
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/ 

# Input: grid = [[1,2],
#                [3,4]]
# Output: [1,4]

# Time Complexity: O(m * n) — we visit every cell in the grid exactly once,
#                  where m = number of rows and n = number of columns.
# Space Complexity: O(m * n) — the result list stores at most ceil(m*n / 2) elements
#                  (every alternate cell is picked); output space dominates.
def zigzagTraversal(grid: list[list[int]]) -> list[int]:
    row = 0 
    col = 0 
    rows = len(grid)
    cols = len(grid[0])
    flag = 0
    isAlternating = False 
    result = [] 
    while row < rows and col < cols:
        if flag == 0:
            for i in range(cols):
                if isAlternating == False:
                    result.append(grid[row][col])
                col += 1 
                isAlternating = not isAlternating 
            flag = 1 
            col -= 1 
        else: 
            for i in range(cols):
                if isAlternating == False:
                    result.append(grid[row][col])
                col -= 1 
                isAlternating = not isAlternating 
            flag = 0
            col += 1 
        row += 1 
    return result

