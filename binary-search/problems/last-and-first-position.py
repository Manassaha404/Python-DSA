# Find First and Last Position of Element in Sorted Array 
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/ 
# [5, 7, 7, 8, 8, 10] -> target = 8
# ans -> [3, 4]

def searchRange(nums: list[int], target: int) -> list[int]:
    low = 0 
    high = len(nums) - 1
    if high < 0:
        return [-1,-1] 
    while low < high:
        mid = low + (high - low) // 2 
        if nums[mid] >= target:
            high = mid 
        else: 
            low = mid + 1 
    starting = high 
    low = 0
    high = len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid 
        else:
            low = mid + 1 
    ending = high - 1 
    if starting <= ending and nums[starting] == target and nums[ending] == target:
        return [starting, ending]
    else:
        return [-1, -1] 

# Time Complexity: O(log n) - two independent binary searches, each O(log n)
# Space Complexity: O(1) - only constant extra variables used

print(searchRange([], 6))