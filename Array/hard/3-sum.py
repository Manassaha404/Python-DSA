# 3 sum 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]] 
# https://leetcode.com/problems/3sum/description/ 
# brute force
# Time Complexity: O(N^3) - three nested loops over the array
# Space Complexity: O(N) - hashSet stores unique triplets (up to N triplets in worst case)
def bruteForceThreeSum(nums:list[int]) -> list[list[int]]:
    hashSet = []
    n = len(nums) 
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    if temp not in hashSet:
                        hashSet.append(temp) 
    ans = list(hashSet) 
    return ans 

print(bruteForceThreeSum([-1,0,1,2,-1,-4])) 


# Time Complexity: O(N^2) - outer loop O(N) * inner loop O(N) with hash set lookups O(1)
# Space Complexity: O(N) - hashSet per outer iteration + result list
def betterThreeSum(nums:list[int]) -> list[list[int]]:
    result = []
    n = len(nums)
    for i in range(n):
        hashSet = set()
        for j in range(i + 1, n):
            k = -(nums[i] + nums[j]) 
            if k in hashSet:
                temp = [nums[i], nums[j], k] 
                temp.sort()
                if temp not in result:
                    result.append(temp) 
            else:
                hashSet.add(nums[j]) 
    return result 

print(betterThreeSum([-1,0,1,2,-1,-4])) 


# Time Complexity: O(N^2) - sorting O(N log N) + O(N) outer loop * O(N) two-pointer inner = O(N^2)
# Space Complexity: O(N) - hashSet stores deduplicated triplets; O(1) auxiliary ignoring output
def threeSum(nums:list[int]) -> list[list[int]]:
    nums.sort() 
    n = len(nums) 
    hashSet = set() 
    for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start = i + 1
        end = n - 1 
        while start < end:
            sum = nums[i] + nums[start] + nums[end] 
            if sum == 0:
                temp = (nums[i] , nums[start] , nums[end])
                if temp not in hashSet:
                    hashSet.add(temp) 
                start += 1
                end -= 1 
            elif sum > 0: 
                end -= 1 
            else:
                start += 1 
    result = [list(t) for t in list(hashSet)] 
    return  result  

print(threeSum([-1,0,1,2,-1,-4])) 



    
