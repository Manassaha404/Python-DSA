# Search in Rotated Sorted Array (without duplicates)
# [4,5,6,7,0,1,2], target = 0 
# ans -> 4 
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/ 
def search(nums:list[int], target:int) -> int:
    low = 0 
    high = len(nums) - 1 
    while low <= high:
        mid = low + (high - low) // 2 
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[low]:
            if nums[mid] < target or target < nums[low]:
                low = mid + 1 
            elif nums[mid] > target and target >= nums[low]:
                high = mid - 1 
        else:
            if nums[mid] > target or target > nums[high]:
                high = mid - 1 
            elif nums[mid] < target and target <= nums[high]:
                low = mid + 1 
    return -1

# Time Complexity: O(log n) - binary search always halves the search space
#                  (guaranteed since there are no duplicates)
# Space Complexity: O(1) - only constant extra variables used

print(search([4,5,6,7,0,1,2], 0))