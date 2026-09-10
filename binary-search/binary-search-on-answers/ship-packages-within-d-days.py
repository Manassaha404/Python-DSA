# Capacity To Ship Packages Within D Days 
# weights = [1,2,3,4,5,6,7,8,9,10], days = 5 
# -> 15 
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/ 


# Time Complexity : O(n) — single pass through the weights array
# Space Complexity: O(1) — only scalar variables used
def dayRequire(weights: list[int], maxWeight:int) -> int:
    day = 0 
    sum = 0
    for weight in weights:
        if sum + weight > maxWeight:
            day += 1 
            sum = 0 
        sum += weight 
    return day + 1

# Time Complexity : O(n * log(sum(weights) - max(weights)))
#   - Binary search range is [max(weights), sum(weights)], so O(log(sum - max)) iterations
#   - Each iteration calls dayRequire which is O(n)
# Space Complexity: O(1) — only scalar variables; no extra data structures used
def shipWithinDays(weights: list[int], days: int) -> int:
    low = max(weights)  
    high = sum(weights) 
    while low <= high:
        mid = low + (high - low) // 2 
        day_require = dayRequire(weights, mid) 
        if day_require > days:
            low = mid + 1 
        else:
            high = mid - 1 
    return low 

print(shipWithinDays([1,2,3,1,1], 4))
        
