# Search in Rotated Sorted Array II (with duplicates) 
# [2,5,6,0,0,1,2], target = 0 
# ans -> true 
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/ 
def search(nums:list[int], target:int) -> int:
    low = 0 
    high = len(nums) - 1 
    while low <= high:
        mid = low + (high - low) // 2 
        if nums[mid] == target:
            return True
        if nums[mid] == nums[low] and nums[low] == nums[high]:
            low += 1 
            high -= 1 
            continue
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
    return False

# Time Complexity: O(log n) average - binary search on rotated array with duplicates
#                  O(n) worst case - when all elements are duplicates (e.g., [1,1,1,1,1]),
#                  the low += 1, high -= 1 shrink reduces search space by 1 at a time
# Space Complexity: O(1) - only constant extra variables used