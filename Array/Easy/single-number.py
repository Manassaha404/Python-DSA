# single number -> 
# https://leetcode.com/problems/single-number/description/ 
# [4,1,2,1,2] -> 4 
# [2,2,1] -> 1 


def singleNumber(nums: list[int]) -> int:
    hashMap = {}
    for num in nums:
        if hashMap.get(num):
            hashMap[num] = hashMap[num] + 1
        else:
            hashMap[num] = 1

    for key in hashMap.keys():
        if hashMap[key] == 1:
            return key 
    return -1

# Time Complexity: O(n) - two separate O(n) passes: one to build the hashmap, one to find the unique key
# Space Complexity: O(n) - hashmap stores at most n/2 + 1 distinct elements

print(singleNumber([2,2,1]))

