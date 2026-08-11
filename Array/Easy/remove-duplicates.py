# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# remove duplicates from a sorted array 
# 0,0,1,1,1,2,2,3,3,4 -> [0,1,2,3,4] -> 5

# Time Complexity  : O(n) — single pass with two pointers i and j over the sorted array
# Space Complexity : O(1) — in-place modification, no extra array allocated
def removeDuplicates(arr:list[int]):
    n = len(arr)
    if n == 1:
        return n 
    i = 0
    j = 1
    while j < n:
        if arr[j] == arr[i]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
            j += 1
    print(arr) 
    return i + 1 

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr))


