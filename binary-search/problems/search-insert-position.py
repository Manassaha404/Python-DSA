# search insert position 
# [5, 6, 7, 8, 9, 10] -> 7
# ans -> 2
# [5, 6, 7, 8, 9, 10] -> 11
# ans -> 6 
#https://leetcode.com/problems/search-insert-position/description/
def searchInsert(arr: list[int], target: int) -> int:
    low = 0 
    high = len(arr)
    while low < high:
        mid = low + (high - low)//2
        if arr[mid] >= target:
            high = mid 
        else:
            low = mid + 1 
    return high 

# Time Complexity: O(log n) - binary search halves the search space each iteration
# Space Complexity: O(1) - only constant extra variables used