# Rearrange Elements By Sign 
# [3,1,-2,-5,2,-4] -> [3,-2,1,-5,2,-4]
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(N) for the result array
def rearrangeArray(nums:list[int]):
    n = len(nums)
    result = [0] * n 
    positive_index = 0
    negative_index = 1 
    for i in range(n):
        if nums[i] < 0:
            result[negative_index] = nums[i] 
            negative_index += 2 
        else:
            result[positive_index] = nums[i] 
            positive_index += 2
    return result

print(rearrangeArray([3,1,-2,-5,2,-4])) 