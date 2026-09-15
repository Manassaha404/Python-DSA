# Median in a Row-Wise Sorted Matrix 
# You are given a 2D integer array matrix of size m x n, where each row is sorted in non-decreasing order,
#  and m * n is odd. Return the median of the matrix.
# matrix = [[1,3,5],
#           [2,6,9],
#           [3,6,9]]
# Output: 5
# Explanation: The sorted array of all elements is [1,2,3,3,5,6,6,9,9], and the median is 5.

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# 1 <= m * n <= 10^6
# 1 <= matrix[i][j] <= 10^6
# matrix[i] is sorted in non-decreasing order.
# m * n is odd.

# Time Complexity  : O(m * n * log(max - min)) — binary search over value range; each step calls countSmallerThanEqualToMid in O(m * log(n))
# Space Complexity : O(1) — no extra space used


# Time Complexity  : O(log(n)) — standard binary search over the sorted row
# Space Complexity : O(1)
def upper_bound(arr:list[int], target:int) -> int:
    low = 0 
    high = len(arr)
    while low < high:
        mid = low + (high - low) // 2 
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1 
    return high 

# Time Complexity  : O(m * log(n)) — calls upper_bound (O(log n)) once per row
# Space Complexity : O(1)
def countSmallerThanEqualToMid(matrix: list[list[int]], midElement: int) -> int:
    count = 0 
    for row in matrix:
        count += upper_bound(row, midElement)
    return count

# Time Complexity  : O(m * log(n) * log(max - min)) — log(max-min) BS iterations, each O(m * log(n))
# Space Complexity : O(1) — constant extra space
def findMedian(matrix: list[list[int]]) -> int:
    m = len(matrix) 
    n = len(matrix[0])
    low = min(matrix[i][0] for i in range(m))
    high = max(matrix[i][n - 1] for i in range(m))
    desired = (m * n) // 2
    while low <= high:
        mid = low + (high - low) // 2 
        if countSmallerThanEqualToMid(matrix, mid) <= desired:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(findMedian([[1,3,5],[2,6,9],[3,6,9]]))  # Output: 5




    