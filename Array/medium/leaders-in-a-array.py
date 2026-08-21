# leaders in a array 
# [1,3,4,22,12,5,7,6] -> [6,7,12,22] 

# Time Complexity: O(N) - single right-to-left pass through the array
# Space Complexity: O(N) - result list stores at most N leaders (output space)
#                  O(1) auxiliary space excluding output
def leaders(nums:list[int]):
    maxi = float("-inf") 
    n = len(nums) 
    result = [] 
    for i in range(n - 1, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i] 
            result.append(maxi) 
    return result 

print(leaders([1,3,4,22,12,5,7,6]))