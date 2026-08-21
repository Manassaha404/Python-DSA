# rotate an array 
# 1 2 3    7 4 1
# 4 5 6 -> 8 5 2 
# 7 8 9    9 6 3 
# https://leetcode.com/problems/rotate-image/description/ 

# Time Complexity: O(N^2) - iterates over roughly half the N*N elements to swap
# Space Complexity: O(1) - in-place transposition, no extra space used
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

# Time Complexity: O(N) - swaps elements from both ends towards the middle
# Space Complexity: O(1) - in-place reversal using a temp variable
def reverse(nums:list[int], start:int, end:int):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

# Time Complexity: O(N^2) - transpose is O(N^2) + N reversal calls each O(N) = O(N^2)
# Space Complexity: O(1) - entire rotation done in-place
def rotateMatrix(matrix:list[list[int]]):
    n = len(matrix)
    transpose(matrix)
    for row in matrix:
        reverse(row, 0, n - 1) 


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix(matrix)
print(matrix) 

    