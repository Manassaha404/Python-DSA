# find sqrt of a number using binary search
# https://leetcode.com/problems/sqrtx/description/
# 25 -> 5
# 28 -> 5
# Time Complexity: O(log n)
# Space Complexity: O(1)
def mySqrt(x: int) -> int:
    if x == 1:
        return 1 
    low = 1 
    high = x // 2 
    while low <= high:
        mid = low + (high - low) // 2 
        if mid * mid > x:
            high = mid - 1 
        else:
            low = mid + 1 
    return high 

print(mySqrt(28))