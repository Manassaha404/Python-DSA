# Single Element in a Sorted Array 
# [1,1,2,3,3,4,4,8,8] -> 2
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/ 
# Time Complexity: O(log n)
# Space Complexity: O(1)
def singleNonDuplicate(nums:list[int]) -> int:
    n = len(nums) 
    if n == 1:
        return nums[0] 
    if nums[0] != nums[1]:
        return nums[0] 
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1] 

    low = 1 
    high = n - 2 
    while low <= high:
        mid = low + (high - low) // 2 
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid] 
        if mid % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                low = mid + 1 
            else:
                high = mid - 1 
        else:
            if nums[mid] == nums[mid - 1]:
                low = mid + 1 
            else:
                high = mid - 1 
    return -1 

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8])) 
            