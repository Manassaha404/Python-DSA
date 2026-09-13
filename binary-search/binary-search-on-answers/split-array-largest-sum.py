#  Split Array Largest Sum 
# Given an integer array nums and an integer k, split nums into k non-empty subarrays 
# such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18

# https://leetcode.com/problems/split-array-largest-sum/description/ 

# Time Complexity: O(n) — single pass through the nums array
# Space Complexity: O(1) — constant extra space
def shouldPartitions(self, nums:list[int], min_sum:int):
    count = 0
    sum_numbers = 0 
    for num in nums:
        if sum_numbers + num > min_sum:
            count += 1 
            sum_numbers = num
        else:
            sum_numbers += num
    return count + 1 


# Time Complexity: O(n log(sum)) — binary search over [max(nums), sum(nums)] range (log(sum) steps),
#                  each step calls shouldPartitions which is O(n).
# Space Complexity: O(1) — only a few variables used, no extra data structures
def splitArray(self, nums: list[int], k: int) -> int:
    n = len(nums) 
    low = nums[0] 
    high = 0 
    for num in nums:
        if low < num:
            low = num 
        high += num 
    while low <= high:
        mid = low + (high - low) // 2 
        should_partition = self.shouldPartitions(nums, mid) 
        if should_partition <= k:
            high = mid - 1 
        else:
            low = mid + 1 
    return low



