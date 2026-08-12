# find missing number -> 
# https://leetcode.com/problems/missing-number/description/
# [3,0,1] -> 2
# [9,6,4,2,3,5,7,0,1] -> 8 

def findMissing(nums:list[int]):
    n = len(nums)
    right_sum = (n*(n + 1))//2 
    actual_sum = 0
    for num in nums:
        actual_sum += num
    missing_number = right_sum - actual_sum 
    return missing_number

# Time Complexity: O(n) - single pass through the array to compute actual_sum
# Space Complexity: O(1) - only a constant number of variables used

print(findMissing([9,6,4,2,3,5,7,0,1]))