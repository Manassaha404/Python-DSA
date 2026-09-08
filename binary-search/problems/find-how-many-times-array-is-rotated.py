# how many times array is rotated 
# [3,4,5,1,2] -> 3 

def findNumberOfRotation(nums: list[int]) -> int:
    low = 0 
    high = len(nums) - 1 
    ans = float("inf")
    rotation_number = 0 
    while low <= high: 
        mid = low + (high - low) // 2 
        if nums[mid] >= nums[low]:
            ans = min(ans, nums[low]) 
            if ans == nums[low]:
                rotation_number = low 
            low = mid + 1 
        else:
            ans = min(nums[mid], ans) 
            if ans == nums[mid]:
                rotation_number = mid
            high = mid - 1 
    return rotation_number  

# Time Complexity: O(log n) - binary search halves the search space each iteration
# Space Complexity: O(1) - only constant extra variables used

print(findNumberOfRotation([4,5,0,1,2,3])) 