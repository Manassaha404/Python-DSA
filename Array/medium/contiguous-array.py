# Given a binary array nums, return the maximum length of a contiguous subarray
#  with an equal number of 0 and 1.
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# https://leetcode.com/problems/contiguous-array/description/ 


# Time Complexity : O(n) — single pass through the array of length n
# Space Complexity: O(n) — hashMap stores at most n+1 distinct prefix sums
def findMaxLength(nums: list[int]) -> int:
    # temp = [] 
    # for i in nums:
    #     if i == 0:
    #         temp.append(-1)
    #     else:
    #         temp.append(1) 

    hashMap = {0:-1}  # maps prefix_sum -> first index it was seen
    longest = 0 
    sum = 0 
    n = len(nums) 
    for i in range(n):
        if nums[i] == 0:
            sum += -1  # treat 0 as -1 so equal 0s and 1s cancel out
        else:
            sum += 1
        if sum in hashMap:
            # same prefix sum seen before → subarray between those indices is balanced
            longest = max(longest, (i - hashMap.get(sum)))
        else:
            hashMap[sum] = i 
    return longest 