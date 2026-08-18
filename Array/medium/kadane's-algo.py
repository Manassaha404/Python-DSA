# sub array with maximum sum
# [-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1] -> 6 

# https://leetcode.com/problems/maximum-subarray/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1)
def maxSum(nums:list[int]):
    max_sum = float('-inf')
    sum = 0
    for num in nums:
        sum += num 
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum


print(maxSum([0,2]))

# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1)
def minSum(nums:list[int]):
    min_sum = float('inf')
    sum = 0
    for num in nums:
        sum += num 
        if sum < min_sum:
            min_sum = sum
        if sum > 0:
            sum = 0
    return min_sum

print(minSum([2,-5,1,-4,3,-2]))


# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1)
def maxAbsoluteSum(nums:list[int]):
    max_sum = float('-inf')
    min_sum = float('inf')
    sum_for_min = 0
    sum_for_max = 0
    for num in nums:
        sum_for_max += num 
        sum_for_min += num
        if sum_for_max > max_sum:
            max_sum = sum_for_max
        if sum_for_min < min_sum:
            min_sum = sum_for_min
        if sum_for_max < 0:
            sum_for_max = 0
        if sum_for_min > 0:
            sum_for_min = 0
    return max(abs(max_sum),abs(min_sum))

print(maxAbsoluteSum([2,-5,1,-4,3,-2]))
        
