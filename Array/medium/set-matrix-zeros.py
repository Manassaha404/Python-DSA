# set matrix zeros -> 
# [1,1,1]     [1,0,1]
# [1,0,1]  -> [0,0,0]
# [1,1,1]     [1,0,1] 
# https://leetcode.com/problems/set-matrix-zeroes/description/

# Time Complexity: O(M * N) - two passes over the entire M x N matrix
# Space Complexity: O(1) - uses the first row and first column as markers (in-place)
def setZeros(matrix:list[list[int]]):
    row_len = len(matrix)
    col_len = len(matrix[0])
    # row_arr = [1] * row_len matrix[..][0]
    # col_arr = [1] * col_len matrix[0][..]
    col0 = 1
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                # row_arr[i] = 0
                # col_arr[j] = 0
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1,row_len):
        for j in range(1,col_len):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
    if matrix[0][0] == 0:
        matrix[0] = [0] * col_len 
    if col0 == 0:
        for i in range(row_len):
            matrix[i][0] = 0
    

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeros(matrix) 
print(matrix) 


