# 0,1,0,3,12 -> 1,3,12,0,0 
# https://leetcode.com/problems/move-zeroes/description/

# Time Complexity  : O(n) — single pass to find first zero + single pass with two pointers
# Space Complexity : O(1) — in-place swaps, no auxiliary storage used

# Helper: swaps two elements in the array in-place
def swap(array:list[int], index1:int, index2:int ):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def moveZero(nums:list[int]):
    n = len(nums)
    firstZeroIndex = -1
    for i in range(n):
        if nums[i] == 0:
            firstZeroIndex = i
            break
    if firstZeroIndex == -1:
        return 
    i = firstZeroIndex + 1
    j = firstZeroIndex

    while i < n:
        if nums[i] != 0:
            swap(nums, i, j)
            i += 1
            j += 1
        else:
            i += 1

a = [0,1,0,3,12]
moveZero(a)
print(a)

    

