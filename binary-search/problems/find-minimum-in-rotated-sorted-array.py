# Find Minimum in Rotated Sorted Array 
# [3,4,5,1,2] -> 1 
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/ 

def findMin(nums: list[int]) -> int:
    low = 0 
    high = len(nums) - 1 
    ans = float("inf")
    while low <= high: 
        mid = low + (high - low) // 2 
        if nums[mid] >= nums[low]:
            ans = min(ans, nums[low]) 
            low = mid + 1 
        else:
            ans = min(nums[mid], ans) 
            high = mid - 1 
    return ans 

# Time Complexity: O(log n) - binary search halves the search space each iteration
# Space Complexity: O(1) - only constant extra variables used

print(findMin([3,4,5,0,1,2])) 

