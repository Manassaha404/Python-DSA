# find majority element which appear more than N/2 times 
# [2,2,1,1,1,2,2] = 2 

# https://leetcode.com/problems/majority-element/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1)
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

        
