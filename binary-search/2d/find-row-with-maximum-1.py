# Row With Maximum Ones

# You are given a binary matrix mat of size m x n, 
# where each row is sorted in non-decreasing order (i.e., all 0's come before all 1's in every row). 
# Return the index of the row that contains the maximum number of 1's. 
# If there are multiple rows with the same maximum count, return the row with the smallest index. 
# If no row contains any 1's, return -1.
# You must solve this O(m log n).
# Example 1:
# Input: mat = [[0,0,0],
#               [1,1,1],
#               [0,1,1]]
# Output: 1
# Explanation: Row 1 has three 1's, which is the maximum. 


# Time Complexity  : O(log n) — binary search over a single row of length n
# Space Complexity : O(1) — no extra space used
def lower_bound(arr:list[int], target:int):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] >= target:
            high = mid - 1 
        else:
            low = mid + 1 
    return low  

# Time Complexity  : O(m * log n) — for each of the m rows, binary search (O(log n)) is performed
# Space Complexity : O(1) — only a constant number of variables used
def rowWithMax1s(mat: list[list[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    max_row_index = -1
    max_count = 0
    for i in range(m):
        count = n - lower_bound(mat[i], 1)
        if count > max_count:
            max_count = count
            max_row_index = i
    return max_row_index

print(rowWithMax1s([[0,0,0],[1,1,1],[0,1,1]]))  # Output: 1  

