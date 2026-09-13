# Kth Missing Positive Number 
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# https://leetcode.com/problems/kth-missing-positive-number/description/ 

# Time Complexity: O(1) — simple arithmetic, no loops
# Space Complexity: O(1) — constant extra space
def missingNumbersTillIndex(index:int, val:int):
    return val - (index + 1) 

# Time Complexity: O(log n) — binary search over the array of length n
# Space Complexity: O(1) — only a few pointers used, no extra data structures
def findKthPositive(arr: list[int], k: int) -> int:
    low = 0 
    high = len(arr) - 1 
    while low <= high:
        mid = low + (high - low) // 2 
        missing_numbers = missingNumbersTillIndex(mid, arr[mid])
        if missing_numbers >= k:
            high = mid - 1 
        else:
            low = mid + 1 
    return arr[high] + (k - missingNumbersTillIndex(high, arr[high]))

print(findKthPositive([2],1))