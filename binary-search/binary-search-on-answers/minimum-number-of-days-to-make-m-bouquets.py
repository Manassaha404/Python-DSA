# Minimum Number of Days to Make m Bouquets
# bloomDay = [1,10,3,10,2], m = 3, k = 1 
# -> 3 
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/ 


# Time Complexity : O(n) — single pass through the bloomDay array
# Space Complexity: O(1) — only scalar counters used
def ifPossible(bloomDay: list[int], m: int, k: int, d:int) -> bool:
    count = 0 
    num_of_bouquets = 0 
    for day in bloomDay:
        if day <= d:
            count += 1 
        else:
            num_of_bouquets += count // k 
            count = 0
    num_of_bouquets += count // k
    if num_of_bouquets >= m:
        return True
    else:
        return False 

# Time Complexity : O(n * log(max(bloomDay) - min(bloomDay)))
#   - Finding min/max is O(n); binary search runs O(log(range)) iterations
#   - Each iteration calls ifPossible which is O(n)
# Space Complexity: O(1) — no auxiliary data structures; only scalar variables used
def minDays(bloomDay: list[int], m: int, k: int) -> int:
    if len(bloomDay) < m * k:
        return -1 
    low = bloomDay[0]
    high = bloomDay[0]
    for day in bloomDay:
        if day < low:
            low = day 
        if day > high:
            high = day 
    while low <= high:
        mid = low + (high - low) // 2 
        is_possible = ifPossible(bloomDay, m, k, mid) 
        if is_possible:
            high = mid - 1 
        else:
            low = mid + 1 
    return low 

print(minDays([1,10,3,10,2],3,1))
