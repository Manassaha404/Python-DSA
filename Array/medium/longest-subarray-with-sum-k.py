# longest sub array with sum k 
# [1,2,3,2,2,3,2,2,1,4,36,7,3,1,1,2], k -> 7 -> 
# possible sub array with sum k -> 
# [2,3,2], [3,2,2], [2,2,3], [2,3,2], [3,2,2],[2,1,4],[7],[3,1,1,2] 
# longest -> [3,1,1,2] len is 4 


# brute force 
def bruteForceLongestSubArray(nums:list[int], k:int):
    n = len(nums)
    longest = 0
    for i in range(n):
        sum = nums[i]
        for j in range(i + 1, n):
            sum += nums[j] 
            if sum >= k:
                subArraySize = j - i + 1
                if sum == k and subArraySize > longest:
                    longest = subArraySize
                break
    return longest

print(bruteForceLongestSubArray([1,2,3,2,2,3,2,2,1,4,36,7,3,1,1,2], 7)) # -> 4
# Time Complexity: O(n^2) 
# Space Complexity: O(1)


# better 
# this include positive and negative number also 
def betterLongestSubArray(nums:list[int], k:int):
    n = len(nums)
    hashMap = {}
    longest = 0
    sum = 0
    for i in range(n):
        sum += nums[i] 
        if sum > k:
            diff = sum - k 
            if hashMap.get(diff):
                start = hashMap.get(diff) + 1
                length = i - start + 1
                if length > longest:
                    longest = length
        if sum == k:
            if i + 1 > longest:
                longest = i 
        hashMap[sum] = i
    return longest
# Time Complexity: O(n)  - single pass through the array
# Space Complexity: O(n) - hashmap stores at most n prefix sums

def betterShortestSubArray(nums:list[int], k:int):
    n = len(nums)
    hashMap = {}
    shortest = float("inf")
    sum = 0
    count_zero = 0
    for i in range(n):
        sum += nums[i] 
        if sum > k:
            diff = sum - k 
            if diff in hashMap:
                start = hashMap.get(diff) + 1
                length = i - start + 1
                if length < shortest:
                    shortest = length
        if sum == k:
            if i + 1 < shortest:
                shortest = i + 1 - count_zero
        if sum != 0:
            hashMap[sum] = i
        if nums[i] == 0:
            count_zero += 1
    return shortest if (shortest != 10**6) else -1
# Time Complexity: O(n)  - single pass through the array
# Space Complexity: O(n) - hashmap stores at most n prefix sums

print(betterShortestSubArray([0,0,69,56,-34], 91))


# https://leetcode.com/problems/subarray-sum-equals-k/description/
def subArraySum(nums:list[int], k:int):
    n = len(nums)
    hashMap = {0: 1}
    arraySum = 0
    sum = 0
    for i in range(n):
        sum += nums[i] 
        prefix_sum = sum - k 
        if prefix_sum in hashMap:
            arraySum += hashMap.get(prefix_sum)
        hashMap[sum] = hashMap.get(sum, 0) + 1
    return arraySum
# Time Complexity: O(n)  - single pass through the array
# Space Complexity: O(n) - hashmap stores at most n prefix sums

print(subArraySum([0,0,0,0,0,0,0,0,0,0], 0))


# only applicable for positives  
def optimalLongestSubArray(nums:list[int], k:int):
    n = len(nums)
    i = 0
    j = 0
    sum = 0
    longest = 0
    while i < n:
        if sum == k:
            if i - j + 1 > longest:
                longest = i - j + 1
        if sum > k and j < n:
            sum -= nums[j]
            j += 1
            continue
        if i < n:
            sum += nums[i]
        i += 1
    return longest
# Time Complexity: O(n)  - two pointers traverse the array at most once each
# Space Complexity: O(1) - only a constant number of variables used

print(optimalLongestSubArray([1,2,3,2,2,3,2,2,1,4,36,7,3,1,1,2], 7)) 


