# find majority element which appear more than N/2 times 
# [2,2,1,1,1,2,2] = 2 

# https://leetcode.com/problems/majority-element/description/
# Time Complexity: O(N) - single pass through the array
# Space Complexity: O(1) - only two variables (element, count) used
def majorityElement(nums:list[int]):
    element = None
    count = 0
    for num in nums:
        if count == 0:
            element = num
            count = 1
        elif num == element:
            count += 1
        else:
            count -= 1
         
    return element

print(majorityElement([2,2,1,1,1,2,2]))


# find elements that appears more than n/3 times 
# [3,2,3] -> [3] 

# Time Complexity: O(N) - two linear passes through the array
# Space Complexity: O(1) - only a fixed number of variables used (el1, el2, count1, count2)
def majorityElement(nums: list[int]) -> list[int]:
    n = len(nums)  
    t = n // 3  
    count1 = 0
    count2 = 0 
    el1 = None 
    el2 = None 
    result = [] 
    for num in nums:
        if count1 == 0 and el2 != num: 
            el1 = num 
            count1 += 1 
        elif count2 == 0 and el1 != num:
            el2 = num 
            count2 += 1 
        elif el1 == num:
            count1 += 1
        elif el2 == num:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0 
    count2 = 0
    for num in nums:
        if num == el1:
            count1 += 1 
        elif num == el2:
            count2 += 1 
    if count1 > t:
        result.append(el1) 
    if count2 > t:
        result.append(el2) 
    return result

        
