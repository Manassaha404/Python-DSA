# Find the Smallest Divisor Given a Threshold 
# nums = [1,2,5,9], threshold = 6 
# -> 5 
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/ 



import math

# Time Complexity : O(n) — iterates through all n numbers once
# Space Complexity: O(1) — only a result accumulator used
def divisionResult(nums:list[int], divisor:int) -> int:
    result = 0 
    for num in nums:
        result += math.ceil(num / divisor)
    return result 


# Time Complexity : O(n * log(max(nums)))
#   - Binary search runs O(log(max(nums))) iterations over [1, max(nums)]
#   - Each iteration calls divisionResult which is O(n)
# Space Complexity: O(1) — only a few scalar variables; no extra data structures
def smallestDivisor(nums: list[int], threshold: int) -> int:
    low = 1 
    high = max(nums) 
    while low <= high:
        mid = low + (high - low) // 2 
        division_result = divisionResult(nums, mid) 
        if division_result <= threshold:
            high = mid - 1
        else:
            low = mid + 1 
    return low 


print(smallestDivisor([44,22,33,11,1], 5))
