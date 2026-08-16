# dutch national flag algo -> 

# [0 0 0 0 0 0 0]   [1 1 1 1 1]     [0 / 1 / 2]      [2 2 2 2 2 2]
#  0 to low - 1    low to mid - 1   mid to high    high + 1 to n -1

# https://leetcode.com/problems/sort-colors/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp




# Time Complexity: O(N) where N is the length of nums
# Space Complexity: O(1) (in-place sorting)
def sortColors(nums:list[int]):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if nums[mid] == 0:
            swap(nums, low, mid)
            low += 1
            mid += 1
            continue
        if nums[mid] == 1:
            mid += 1
            continue
        if nums[mid] == 2:
            swap(nums, mid, high)
            high -= 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
