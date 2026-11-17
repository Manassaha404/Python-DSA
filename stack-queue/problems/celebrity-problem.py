# Celebrity Problem
# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

# Time Complexity  : O(N) — two-pointer elimination takes O(N) comparisons and candidate verification takes O(N) checks, where N is the number of people (matrix is N x N)
# Space Complexity : O(1) — constant auxiliary space used for two pointers
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        top = 0
        bottom = n - 1
        while top < bottom:
            if mat[top][bottom] == 1:
                top += 1
            elif mat[bottom][top] == 1:
                bottom -= 1
            else:
                top += 1
                bottom -= 1
        if top == bottom:
            for i in range(n):
                if mat[top][i] == 1 and top != i:
                    return -1
                if mat[i][top] == 0:
                    return -1
            return top
        else:
            return -1 