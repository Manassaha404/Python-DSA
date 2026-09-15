# Find a Peak Element II 
# matrix = [[1,4,3],[6,5,2]], Output: [1,0] or [0,1]
# https://leetcode.com/problems/find-a-peak-element-ii/description/
# Time Complexity  : O(m * log(n)) — binary search on each row to find a peak element
# Space Complexity : O(1) — no extra space used


# Time Complexity  : O(m) — linear scan over all rows for the given column
# Space Complexity : O(1) — constant extra space
def findMaxRowIndex(self, mat: list[list[int]], col:int, n:int) -> int:
    maxRowIndex = 0 
    maxRowEl = mat[0][col] 
    for i in range(n):
        if mat[i][col] > maxRowEl:
            maxRowEl = mat[i][col] 
            maxRowIndex = i 
    return maxRowIndex 

# Time Complexity  : O(m * log(n)) — log(n) binary search iterations, each calling findMaxRowIndex in O(m)
# Space Complexity : O(1) — no auxiliary data structures
def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
    m = len(mat) 
    n = len(mat[0]) 
    low = 0 
    high = n - 1 
    while low <= high:
        mid = low + (high - low) // 2 
        maxRowIndex = self.findMaxRowIndex(mat, mid, m)
        left = -1 
        right = -1 
        if mid - 1 >= 0:
            left = mat[maxRowIndex][mid - 1] 
        if mid + 1 < n:
            right = mat[maxRowIndex][mid + 1] 
        if left < mat[maxRowIndex][mid] > right:
            return [maxRowIndex, mid] 
        elif mat[maxRowIndex][mid] < left:
            high = mid - 1 
        else:
            low = mid + 1 
    return [-1,-1]