# next permutation -> 
# [1,2,3] -> [1,3,2] 
# https://leetcode.com/problems/next-permutation/description/


# Time Complexity: O(N) where N is the length of the reversed portion
# Space Complexity: O(1)
def reverse(nums:list[int], start:int, end:int):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

# Time Complexity: O(1)
# Space Complexity: O(1)
def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1) (in-place)
def nextPermutation(nums:list[int]):
    n = len(nums) 
    deep_index = -1 
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i + 1]:
            deep_index = i 
            break
    if deep_index == -1:
        reverse(nums, 0, n -1)
        return
    swap_index = -1
    for i in range(n - 1, deep_index - 1,-1):
        if nums[i] > nums[deep_index]:
            swap_index = i
            break
    swap(nums, deep_index, swap_index)
    reverse(nums, deep_index + 1, n - 1)

nums = [1,2,3]
nextPermutation(nums)
print(nums) 
    
    
        
    