# find nth root of a number using binary search
# 69 , 4 -> -1 
# 16 , 4 -> 2
# 81 , 4 -> 3
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findNthRoot(x: int, n: int) -> int:
    if x == 1:
        return 1 
    low = 1 
    high = x // n
    while low <= high:
        mid = low + (high - low) // 2 
        if mid ** n > x:
            high = mid - 1 
        elif mid ** n < x:
            low = mid + 1 
        else:
            return mid 
    return -1

print(findNthRoot(81, 4))