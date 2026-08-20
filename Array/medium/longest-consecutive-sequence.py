# longest consecutive sequence 
# [100,4,200,1,3,2] -> 4 ([1,2,3,4]) 
# https://leetcode.com/problems/longest-consecutive-sequence/description/



# def longestConsecutive(nums:list[int]) -> int:
#     n = len(nums) 
#     hashMap = {} 
#     for i in range(n):
#         if nums[i] not in hashMap:
#             hashMap[nums[i]] = i
#     longest = 0
#     for key in list(hashMap.keys()):
#         isIn = True
#         count = 1
#         if (key - 1) not in hashMap:
#             while isIn:
#                 if (key + 1) in hashMap:
#                     count += 1 
#                     key += 1 
#                 else:
#                     isIn = False
#         longest = max(longest, count) 
#     return longest 

def longestConsecutive(nums:list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for key in numSet:
            if (key - 1) not in numSet:
                count = 1
                while (key + count) in numSet:
                    count += 1
                longest = max(longest, count)
        return longest


print(longestConsecutive([1,0,1,2])) 
                
        
    




