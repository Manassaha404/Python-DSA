# Search a 2D Matrix 
# matrix = [[1,3,5,7],[10,11,16,20], [23,30,34,60]], target = 3 
# Output: true 
# https://leetcode.com/problems/search-a-2d-matrix/description/ 
# Time Complexity  : O(log(m * n)) — treats the m×n matrix as a flattened sorted array and binary searches it
# Space Complexity : O(1) — no extra space used
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix) 
    n = len(matrix[0]) 
    low = 0 
    high = (m * n) - 1 
    while low <= high:
        mid = low + (high - low) // 2 
        el = matrix[mid // n][mid % n] 
        if el == target:
            return True 
        elif el < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return False


# Search a 2D Matrix II 
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# Time Complexity  : O(m + n) — starts from top-right corner, each step eliminates a row or column
# Space Complexity : O(1) — no extra space used
def searchMatrixII(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix) 
    n = len(matrix[0]) 
    row = 0 
    col = n - 1 
    while row < m and col >= 0:
        el = matrix[row][col] 
        if el == target:
            return True
        elif el < target:
            row += 1
        else:
            col -= 1
    return False