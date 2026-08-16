# Two Sum -> 
# [2,7,11,15], target = 9 
# -> [0,1] 
# https://leetcode.com/problems/two-sum/description/
nums = [3,2,4]
target = 6
# brute force 
# Time Complexity: O(N^2) where N is the length of nums
# Space Complexity: O(1)
def bruteForceTwoSum(nums:list[int], target:int):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]


print(bruteForceTwoSum(nums,target))


# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(N) due to hash map
def betterTwoSum(nums:list[int], target:int):
    n = len(nums)
    hashMap = {}
    for i in range(n):
        diff = target - nums[i] 
        if diff in hashMap:
            return [hashMap.get(diff), i]
        hashMap[nums[i]] = i 

print(betterTwoSum(nums, target))


# if the given array is sorted 
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1)
def sortedTwoSum(nums:list[int], target:int):
    n = len(nums) 
    i = 0
    j = n - 1
    while i < j:
        sum = nums[i] + nums[j]
        if sum == target:
            return [i+1,j+1] 
        if sum > target:
            j -= 1
            continue
        if sum < target:
            i += 1

print(sortedTwoSum([2,7,11,15], 9))


            