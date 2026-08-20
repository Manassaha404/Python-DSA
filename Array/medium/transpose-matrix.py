# transpose a matrix 
# 1 2 3     1 4 7
# 4 5 6  -> 2 5 8 
# 7 8 9     3 6 9 


def transpose(matrix:list[list[int]]):
    row_length = len(matrix) 
    col_length = len(matrix[0])
    if row_length != col_length:
        print("matrix is not a square matrix")
        return
    for i in range(row_length - 1):
        for j in range(i + 1, row_length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)
print(matrix) 

    